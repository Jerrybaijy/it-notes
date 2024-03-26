# Docker基础

​	Docker 是一个开源的平台，用于开发、交付和运行应用程序。它使用容器技术，通过将应用程序及其依赖项打包到一个容器中，提供了轻量级、可移植和自包含的环境。

## 环境搭建

### Windows 环境

1. 确保 Windows 中已部署WSL

2. 确保 Linux 升级至最新版并运行

3. 确保 Docker Desktop 已安装并运行

4. 启动  `sudo dockerd`


### Linux 环境

1. 下载 Docker 安装脚本并执行：

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

2. 将用户添加到 `docker` 用户组：

   ```bash
   sudo usermod -aG docker $USER
   ```

3. 退出当前终端并重新登录，或者执行下面的命令使用户组更改生效：

   ```bash
   newgrp docker
   ```

4. 验证 Docker 安装：

   ```bash
   docker --version
   ```

5. 启动 Docker

   ```bash
   sudo systemctl start docker
   ```

6. 验证 Docker 服务状态

   ```bash
   sudo systemctl status docker
   ```

7. 将 Docker 添加到开机启动

   ```bash
   sudo systemctl enable docker
   ```

8. 登录

   ```bash
   docker login
   ```

## Docker 管理

- **Docker 管理**

  ```bash
  # 查看 Docker 版本信息
  docker -v
  # 显示 Docker 详细版本信息
  docker version
  # 显示 Docker 系统信息
  docker info
  # 登录和登出
  docker login
  docker logout
  ```

## 基本流程

1. 本地已安装并启动登录 Docker
2. 创建项目
5. 项目根目录创建 Dockerfile

4. 终端进入文件夹 HelloDocker 目录
7. 构建推送镜像

   - 手动构建构建镜像保存至本地，加标签，然后手动推送至 DockerHub
   - 通过 GitLab Pipeline 自动构建镜像并自动推送至 DockerHub
8. 运行容器

   - 从本地 image 运行容器
   - 从 DockerHub 拉取 image 运行容器

# [镜像](https://docs.docker.com/reference/cli/docker/image/)

## 镜像基础

- **基础命令**

  ```bash
  # 查看镜像
  docker images
  # 从 Dockerfile 创建镜像
  docker build -t $IMAGE_NAME[:$TAG] $PATH
  # 从容器提交创建镜像
  docker commit $CONTAINER_NAME $IMAGE_NAME[:$TAG]
  # 删除镜像
  docke rmi $IMAGE_NAME[:$TAG]
  # 删除全部镜像
  docker rmi -f $(docker images -aq)
  # 拉取镜像
  docker pull $REPO_NAME/$IMAGE_NAME:$TAG
  # 推送镜像
  docker push $REPO_NAME/$IMAGE_NAME:$TAG
  ```

- **标签**

  ```bash
  # 加标签
  docker tag $IMAGE_NAME:$TAG $REPO_NAME/$IMAGE_NAME:$TAG
  ```

## 其它

# [容器](https://docs.docker.com/reference/cli/docker/container/)

## 容器基础

- **基础命令**

  ```bash
  # 查看容器
  docker ps [-a] # -a表示全部，包含未运行
  # 创建容器
  docker create $IMAGE
  # 启动容器
  docker start $CONTAINER_NAME
  # 创建并启动容器
  docker run [-d] [-it] --name $CONTAINER_NAME $IMAGE
  # 重启容器
  docker restart $CONTAINER_NAME
  # 停止容器
  docker stop $CONTAINER_NAME
  # 删除容器
  docker rm $CONTAINER_NAME
  # 删除全部容器
  docker rm $(docker ps -aq)
  ```

## 其它

- **其它命令**

  ```bash
  # 查看容器日志
  docker logs [OPTIONS] CONTAINER
  # 检查容器详细信息
  docker container inspect [OPTIONS] CONTAINER [CONTAINER...]
  ```
  
- **进入容器执行**

  ```bash
  docker exec [OPTIONS] CONTAINER [COMMAND] [ARG...]
  # eg：进入容器的 shell 环境
  docker exec -it jerry-container /bin/sh
  # eg：进入容器的 bash 环境
  docker exec -it jerry-container bash
  ```

- [**复制文件**](https://docs.docker.com/reference/cli/docker/container/cp/)

  在容器和本地文件系统之间复制，容器之间不能直接复制

  ```bash
  docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
  ```


# 命令选项

- **-a (--all)**：

  - 对于镜像：列出本地所有镜像，包括中间层
  - 对于容器：显示所有容器（否则仅显示运行容器）

- [**-c (--change)**](https://docs.docker.com/reference/cli/docker/container/commit/#change)：将 Dockerfile 指令应用于创建的镜像

- **[-d (--detach)](https://docs.docker.com/reference/cli/docker/container/run/#detach)**：在后台运行容器，不占用终端

- [**-e (--env ; --env-file)**](https://docs.docker.com/reference/cli/docker/container/run/#env)：设置环境变量

- [**--entrypoint /bin/sh**](https://docs.docker.com/compose/compose-file/05-services/#entrypoint)：设置容器的入口点，后面的值 `/bin/sh` 表示启动容器后直接进入 Shell 环境。

- [**-f (--force)**](https://docs.docker.com/reference/cli/docker/container/rm/#force)：强制删除运行中的容器

- **-it**：(-i 和 -t 的组合)

  - [**-t (--tty)**](https://docs.docker.com/reference/cli/docker/container/run/#tty)：分配一个伪终端 (TTY) 给容器，这样可以在容器中执行交互式的命令
  - [**-i (--interactive)**](https://docs.docker.com/reference/cli/docker/container/run/#interactive)：让容器的标准输入保持打开，以便我们可以与容器进行交互

- [**--name**](https://docs.docker.com/reference/cli/docker/container/run/#name)：命名容器

- [**-p (--publish)**](https://docs.docker.com/reference/cli/docker/container/run/#publish)：端口映射

  ```bash
  -p $HOST_PORT:$CONTAINER_PORT
  # eg
  -p 80:8080
  ```

- [**`-t $IMAGE_NAME[:$TAG]`**](https://docs.docker.com/reference/cli/docker/image/build/#tag)：命名镜像（-t / --tag），可一次使用多个 `-t`

# Dockerfile

​	Dockerfile 文件用于构建 docker 镜像，文件中包含了镜像的各种配置信息。

## 关键部分

1. **基础镜像（Base Image）**：选择适合你应用程序的基础镜像作为起点。基础镜像是构建你的镜像的基础，通常包含了操作系统和一些基本的软件工具。在示例中，我们选择了Python官方提供的3.9版本的镜像作为基础。

   ```dockerfile
   FROM <image_name>:<tag> as builder
   # eg
   FROM python:3.9-slim as builder
   ```

2. **设置工作目录**：设置容器内的工作目录

   ```dockerfile
   WORKDIR /app
   ```

3. **依赖安装（Dependency Installation）**：如果你的应用程序依赖于其他软件包或库，你需要在Dockerfile中安装它们。通常会使用`RUN`命令运行适当的安装命令，如`pip install`用于Python依赖。

   ```dockerfile
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   ```

   - Python使用`pip install`安装依赖
   - 将当前目录下的`requirements.txt`文件复制到容器的`/app`目录中，这个文件列出了Python依赖

   - 使用pip安装`requirements.txt`中列出的Python依赖，`--no-cache-dir`参数用于避免缓存。

   ```dockerfile
   RUN go mod init hello-app
   ```

   - 在 Go 项目中，使用`go mod init`初始化一个名为 "hello-app" 的 Go 模块。这会在你的项目目录下生成一个 `go.mod` 文件，其中记录了你的项目的依赖。接下来，当你运行 `go build` 时，Go 工具会根据 `go.mod` 文件自动下载并安装依赖。

4. **复制文件（File Copying）**：将应用程序的文件复制到镜像中。这可能包括应用程序代码、配置文件、静态资源等。使用`COPY`或`ADD`命令将这些文件从本地文件系统复制到镜像中。

   ```dockerfile
   COPY server.py .
   ```

   将当前目录下的`server.py`文件复制到容器的`/app`目录中。

5. **环境配置（Environment Configuration）**：配置容器内部的环境变量，以确保应用程序能够正确运行。这可能包括端口号、数据库连接信息等。使用`ENV`命令设置环境变量。

   ```dockerfile
   ENV PORT 8080
   ```

   设置名为`PORT`的环境变量，并将其值设为8080。

6. **启动命令（Startup Command）**：定义容器启动时的默认命令。这是告诉Docker容器应该运行哪个应用程序的关键部分。使用`CMD`或`ENTRYPOINT`命令定义启动命令。

   ```dockerfile
   CMD ["python", "server.py"]
   ```

   定义容器启动时的默认命令，即运行`python server.py`来启动Python应用程序。

## 字段说明

- **ENTRYPOINT**：设置容器的入口点

## 相关项目

- Dockerfile Build Image

## 手动训练

1. 这个训练用于手动模拟 Dockerfile 文件创建一个容器化应用的过程。

2. 下载 main.go 至本地 hello 文件夹

   - **文件来源**：[GoogleCloudPlatform/kubernetes-engine-samples/quickstarts/hello-app/](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/da3e2c22c727e3b6d72d4eea04c19335db0727cb/quickstarts/hello-app)

   - 与 Dockerfile Build Image 项目使用相同文件

   - Linux 下载

     ```bash
     curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/main/quickstarts/hello-app/main.go
     ```

   - main.go

     ```go
     package main
     
     import (
     	"fmt"
     	"log"
     	"net/http"
     	"os"
     )
     
     func main() {
     	mux := http.NewServeMux()
     	mux.HandleFunc("/", hello)
     
     	port := os.Getenv("PORT")
     	if port == "" {
     		port = "8080"
     	}
     
     	log.Printf("Server listening on port %s", port)
     	log.Fatal(http.ListenAndServe(":"+port, mux))
     }
     
     func hello(w http.ResponseWriter, r *http.Request) {
     	log.Printf("Serving request: %s", r.URL.Path)
     	host, _ := os.Hostname()
     	fmt.Fprintf(w, "你好, 世界!\n")
     	fmt.Fprintf(w, "Version: 1.0.0\n")
     	fmt.Fprintf(w, "Hostname: %s\n", host)
     }
     ```

   - Dockerfile

     ```dockerfile
     FROM golang:1.21.0 as builder
     WORKDIR /app
     RUN go mod init hello-app
     COPY *.go ./
     RUN CGO_ENABLED=0 GOOS=linux go build -o /hello-app
     
     FROM gcr.io/distroless/base-debian11
     WORKDIR /
     COPY --from=builder /hello-app /hello-app
     ENV PORT 8080
     USER nonroot:nonroot
     CMD ["/hello-app"]
     ```

3. 模拟 Dockerfile

   ```bash
   #本地全程都在 hello 目录下操作
   
   # 编译环境
   # 创建编译环境容器
   docker run -d -it --name builder golang:1.21.0
   # 进入编译环境容器的 bash 环境
   docker exec -it builder /bin/sh
   # 进入根目录
   cd /
   # 创建工作目录app
   mkdir app
   # 模块化
   go mod init hello-app
   # 退出编译环境容器
   exit
   # 复制 main.go 至容器内的工作目录 app
   docker cp *.go builder:/app
   # 进入编译环境容器
   docker exec -it builder bash
   cd /app
   # 编译你的 Go 应用程序为静态 Linux 可执行文件。然后，你将编译好的可执行文件保存为 /hello-app。
   CGO_ENABLED=0 GOOS=linux go build -o /hello-app
   exit
   
   
   # 生产环境
   # 创建生产环境：通过将应用程序从 builder 镜像中复制到这个镜像中，并设置相应的运行时配置，最终生成的镜像将是一个精简的、只包含应用程序和运行时环境的最小化镜像，从而降低了攻击面和维护成本。
   # 由于不允许运行，我使用了一个新image
   docker run -d -it -p 80:8080 --name runner debian
   # 从编译环境中复制应用程序 hello-ap 到生产环境，由于容器之间不能直接复制，所以以本机作为中转
   docker cp builder:/hello-app .
   docker cp hello-app runner:/hello-app
   
   # 进入生产环境容器的 bash 环境
   docker exec -it runner bash
   # 暴露生产环境的8080端口
   export PORT=8080
   # 添加nonroot用户
   adduser --disabled-password --gecos "" nonroot
   # 运行应用程序
   /hello-app
   ```

4. 访问应用

   ```bash
   # 在容器内访问应用，新建终端，容器环境内有 curl 工具
   curl http://127.0.0.1:8080
   # 在Linux中访问应用
   curl http://127.0.0.1:80
   ```

5. 如果想把 runner 容器 commit 成 Image

   ```bash
   # 创建 Image
   docker commit -c 'ENTRYPOINT ["/hello-app"]' runner $IMAGE_NAME
   # 运行新容器
   docker run -d -it -p 80:8080 --name $CONTAINER_NAME $IMAGE_NAME
   # 随后即可访问
   ```

# 其它



