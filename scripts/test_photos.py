"""Tests for scripts/photos.py.

    uv run --with pillow --with pyyaml --with pytest pytest scripts/test_photos.py
"""

from fractions import Fraction
from pathlib import Path

import pytest
import yaml
from PIL import ExifTags, Image
from PIL.TiffImagePlugin import IFDRational as R

import photos


@pytest.fixture
def site(tmp_path, monkeypatch):
    """Point the script at a throwaway site root."""
    (tmp_path / "_data").mkdir()
    monkeypatch.setattr(photos, "ROOT", tmp_path)
    monkeypatch.setattr(photos, "OUT_DIR", tmp_path / "images" / "photos")
    monkeypatch.setattr(photos, "META_FILE", tmp_path / "_data" / "photo_meta.yml")
    monkeypatch.setattr(photos, "LIST_FILE", tmp_path / "_data" / "photos.yml")
    return tmp_path


def make_jpeg(path: Path, size=(1200, 900), orientation=None, gps=True) -> Path:
    im = Image.new("RGB", size, (40, 120, 200))
    exif = Image.Exif()
    exif[photos.TAG["Make"]] = "SONY"
    exif[photos.TAG["Model"]] = "ILCE-7CM2"
    if orientation:
        exif[photos.TAG["Orientation"]] = orientation
    sub = exif.get_ifd(ExifTags.IFD.Exif)
    sub[photos.TAG["DateTimeOriginal"]] = "2026:09:06 17:23:48"
    sub[photos.TAG["FNumber"]] = R(28, 10)
    sub[photos.TAG["ExposureTime"]] = R(1, 1000)
    sub[photos.TAG["FocalLength"]] = R(70, 1)
    sub[photos.TAG["ISOSpeedRatings"]] = 50
    sub[photos.TAG["LensModel"]] = "FE 24-70mm F2.8 GM II"
    if gps:
        g = exif.get_ifd(ExifTags.IFD.GPSInfo)
        g[1], g[2] = "N", (R(21, 1), R(12, 1), R(0, 1))
        g[3], g[4] = "W", (R(86, 1), R(44, 1), R(0, 1))
    im.save(path, "JPEG", exif=exif)
    return path


def test_shutter_formats():
    assert photos.shutter(Fraction(1, 1000)) == "1/1000 s"
    assert photos.shutter(0.0015625) == "1/640 s"
    assert photos.shutter(2) == "2 s"
    assert photos.shutter(None) is None


def test_add_writes_variants_without_metadata(site, tmp_path):
    src = make_jpeg(tmp_path / "DSC00001.jpg")
    photos.add([src])

    variants = sorted((site / "images" / "photos").glob("DSC00001-*.webp"))
    # 1200px source: the 800 variant plus one full-size copy; no duplicate upscales.
    assert [p.name for p in variants] == ["DSC00001-1200.webp", "DSC00001-800.webp"]
    for variant in variants:
        with Image.open(variant) as im:
            assert not im.getexif(), "EXIF (incl. GPS) must not survive into published files"
            assert "exif" not in im.info

    meta = yaml.safe_load((site / "_data" / "photo_meta.yml").read_text())["DSC00001"]
    assert meta["widths"] == [800, 1200]
    assert (meta["width"], meta["height"]) == (1200, 900)
    assert meta["camera"] == "Sony α7C II"
    assert meta["taken"] == "2026-09-06"
    assert (meta["aperture"], meta["shutter"], meta["iso"]) == ("f/2.8", "1/1000 s", 50)
    assert meta["color"].startswith("#") and len(meta["color"]) == 7
    assert "gps" not in str(meta).lower()


def test_add_appends_one_stub_per_new_photo(site, tmp_path):
    src = make_jpeg(tmp_path / "DSC00002.jpg")
    photos.add([src])
    photos.add([src])  # re-processing must not duplicate the hand-edited entry
    entries = yaml.safe_load((site / "_data" / "photos.yml").read_text())
    assert [e["id"] for e in entries] == ["DSC00002"]


def test_existing_entries_are_left_untouched(site, tmp_path):
    listing = site / "_data" / "photos.yml"
    listing.write_text("# my notes\n- id: DSC00003\n  title: Kept as written\n")
    photos.add([make_jpeg(tmp_path / "DSC00003.jpg")])
    assert listing.read_text() == "# my notes\n- id: DSC00003\n  title: Kept as written\n"


def test_exif_orientation_is_applied(site, tmp_path):
    src = make_jpeg(tmp_path / "DSC00004.jpg", size=(1200, 900), orientation=6)
    photos.add([src])
    meta = yaml.safe_load((site / "_data" / "photo_meta.yml").read_text())["DSC00004"]
    assert (meta["width"], meta["height"]) == (900, 1200)


def test_social_card_is_1200x630(site, tmp_path):
    photos.add([make_jpeg(tmp_path / "DSC00005.jpg", size=(3000, 2000))])
    photos.social("DSC00005", focus_y=0.3)
    with Image.open(site / "images" / "og-image.jpg") as im:
        assert im.size == (1200, 630)


def test_missing_source_is_an_error(site, tmp_path):
    with pytest.raises(SystemExit):
        photos.add([tmp_path / "nope.jpg"])


def test_social_without_variants_is_an_error(site):
    with pytest.raises(SystemExit):
        photos.social("DSC99999", focus_y=0.5)
