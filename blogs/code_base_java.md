Read file line by line
```
try (BufferedReader br = new BufferedReader(new FileReader(file))) {
    String line;
    while ((line = br.readLine()) != null) {
       // process the line.
    }
}
```

Write file
```
try (PrintWriter outToResult = new PrintWriter(new BufferedWriter(new FileWriter("test_out.txt", true)))) {
    ...
} catch (Exception e) {
    e.printStackTrace();
}
```
