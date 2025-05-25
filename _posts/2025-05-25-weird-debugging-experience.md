---
layout: single
title:  "A weird debugging process for Jupyter Notebook on WSL 2"
date: 2025-05-25 
categories: 
  - Random
tags:
  - debugging
---

事情的起因是：
在 WSL 2 下开启 Jupyter Notebook, 在 windows 下可以通过 127.0.0.1:8888 启动，但无法通过 localhost:8888 启动。

当时我就觉得特别奇怪，因为在我的认知里，localhost 就会被直接解析为 127.0.0.1. 于是我拿着这个问题去问 ChatGPT, Claude, 和 Gemini。最终的结论是，没有一个大模型能真正地端到端帮我解决这个问题，但是他们都或多或少给了我一些 insights 让我最终找到这个问题的根因。

所有的大模型，都提到了在 windows 下 ipv4 和 ipv6 的解析问题。原来，在 windows 下如果我们不去改 hosts 文件，浏览器会在localhost下优先解析 ipv6 的地址，而 jupyter notebook 没有在 ipv6 监听，于是得到 404.

事情真的这么简单吗？那按道理来说，只要我强制 loopback 先去解析 ipv4 地址，问题就应该解决了？或者是我索性直接让 loopback 不要去解析 ipv6，也可以？于是我先尝试了：
`netsh interface ipv6 set prefixpolicy ::ffff:0:0/96 60 0`

这个命令是在 dual stack 系统中，让 ipv4 的地址解析优先级显著高于 ipv6，虽然我也不知道到底有没有用，但结果是当我使用 localhost:8888 时，仍然是 404. 并且我能看到在 dev tools 中，http header 的 remote addr 是`[::1]:8888`，意味着 localhost 还是被解析为 ipv6 地址，且返回了 404.

但是如果这个地址+端口没有任何进程在监听，chrome 根本不会显示 404 啊？它只会没有响应。

况且更诡异的是，在调试过程中，我打开了 Python simple httpserver 在 8000 端口，不管是 localhost 还是 127.0.0.1 都没有问题。于是我被带到这是 jupyter notebook 的问题，需要升级至 7.2.0 才能支持 dual stack 且不会拒绝远程网络的访问，等等。

最关键的来了，我通过 curl 命令来访问 localhost 和 127.0.0.1 （均为 ipv4）时，其实都可以访问 jupyter notebook 的服务器。

![curl 命令关键时候很好用]({{ site.baseurl }}/images/Pasted-image-20250525173534.png)

这就意味着，其实只要我用 ipv4 的 localhost, jupyter 不会拒绝，没有什么 remote access 拒绝的问题。

在我走投无路准备放弃以后就使用 ip 地址时，我搜了搜 google，找到了这个问题：

[WSL2: localhost:8888 stopped working](https://superuser.com/questions/1878272/wsl2-localhost8888-stopped-working)

看描述简直和我一模一样，于是我就换了个端口，结果就可以访问了。。。

于是我再接再厉，把这个 prompt 放到了 O3 里：

> [!NOTE] 我给 O3 的最后一击
> Surprisingly, if i start jupyter with another port say 9999, then both localhost and 127.0.0.1 works, why??

O3 的回复是：


![O3 的回复]({{ site.baseurl }}/images/Pasted-image-20250525174008.png)

事情到这里就很清楚了，有另一个进程一直在监听 ipv6 的 localhost ... 而这个进程是——docker desktop!!! 

[我也不知道 docker 为什么要设置到 8888 去](https://forums.docker.com/t/docker-listening-on-port-8888-after-latest-update-no-running-containers/144633/3)

于是把 docker 的这个选相关了，就没有人再占用 8888 了，事情从此太平。

回头思考整个过程，我觉得大模型还是帮助了我很多。在这个过程中，我主要使用的模型是 O3，O3 现在比较 Agentic 每次会搜索很多网页来增加他回答的可信度。如果没有大模型，在这个过程中，我可能就放弃这个问题了，因为实在也没有必要。支撑我继续解决这个问题是我想看看每次我在给出反馈后大模型究竟会怎么应对。作为 Reference, 我把整个和 O3 的交流分享在[这里](https://chatgpt.com/share/68339888-5fe0-8002-8e25-6732319bae01).
