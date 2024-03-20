# Docker基础

​	Docker 是一个开源的平台，用于开发、交付和运行应用程序。它使用容器技术，通过将应用程序及其依赖项打包到一个容器中，提供了轻量级、可移植和自包含的环境。

## 环境搭建

### Windows 环境

1. 确保 Windows 中已部署WSL

2. 确保 Linux 升级至最新版并运行

3. 确保 Docker Desktop 已安装并运行

4. 启动  `sudo dockerd`

   在 WSL 上，Docker 通过 Windows 的 Docker Desktop 软件来管理，而不是作为一个独立的系统服务。因此，你不需要像在传统的 Linux 环境中那样使用 `service` 命令。

   在 WSL 中使用 Docker，你可以直接运行 Docker 的启动命令 `sudo dockerd`。

### Linux 环境

#### 使用官方安装脚本

1. 安装 curl

   ```bash
   sudo snap install curl
   ```

2. 下载 Docker 安装脚本并执行：

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

3. 将用户添加到 `docker` 用户组：

   **注意：**将 `$USER` 换成 Linux 系统的用户名，如 jerry

   ```bash
   sudo usermod -aG docker $USER
   ```

4. 退出当前终端并重新登录，或者执行下面的命令使用户组更改生效：

   ```bash
   newgrp docker
   ```

5. 验证 Docker 安装：

   ```bash
   docker --version
   ```

6. 启动 Docker

   ```bash
   sudo systemctl start docker
   ```

7. 验证 Docker 服务状态

   ```bash
   sudo systemctl status docker
   ```

8. 将 Docker 添加到开机启动

   ```bash
   sudo systemctl enable docker
   ```

#### 使用包管理器安装

- 在 Alpine Linux 上安装 Docker 可以使用 Alpine 包管理器 apk 来完成

  ```bash
  apk add docker
  ```

- 不同发行版的 Linux 中，Docker 的命令也不同

## Docker 管理

- **Docker 管理**

  ```bash
  # 显示 Docker 版本信息
  docker version
  # 显示 Docker 系统信息
  docker info
  # 登录和登出
  docker login
  docker logout
  ```

## 完整流程

### 在本地运行容器

1. 本地已安装并启动 Docker

2. VS Code 中安装 Docker 扩展

3. 创建项目文件夹 hello-docker，并在 VS Code 中打开文件夹

4. 创建文件 index.js

   ```javascript
   console.log("欢迎光临")
   ```

5. 创建文件 Dockerfile

   ```dockerfile
   FROM node:14-alpine
   COPY index.js /index.js
   CMD node /index.js
   ```

6. 终端进入文件夹 HelloDocker 目录

7. 构建镜像

   ```bash
   docker build -t hello-docker .
   ```

8. 运行容器

   ```bash
   docker run hello-docker
   ```

9. 停止容器

   ```bash
   docker stop 7cada994ddf5
   ```

### 推送和拉取

1. 登录

   ```bash
   docker login
   ```

2. 加标签

   ```bash
   docker tag hello-docker:latest jerrybaijy/hello-docker:v1.0
   ```

3. 推送镜像

   ```bash
   docker push jerrybaijy/hello-docker:v1.0
   ```

4. 拉取镜像

   ```bash
   docker pull jerrybaijy/hello-docker:v1.0
   ```

   

# [镜像](https://docs.docker.com/reference/cli/docker/image/)

## 镜像基础

- **基础命令**

  ```bash
  # 查看镜像
  docker images
  # 从 Dockerfile 创建镜像
  docker build -t IMAGE_NAME[:TAG] PATH
  # 从容器提交创建镜像
  docker commit CONTAINER_NAME IMAGE_NAME[:TAG]
  # 删除镜像
  docke rmi IMAGE_NAME[:TAG]
  # 删除全部镜像
  docker rmi -f $(docker images -aq)
  # 拉取镜像
  docker pull REPO_NAME/IMAGE_NAME:TAG
  # 推送镜像
  docker push REPO_NAME/IMAGE_NAME:TAG
  ```

- **标签**

  ```bash
  # 加标签
  docker tag IMAGE_NAME:TAG REPO_NAME/IMAGE_NAME:TAG
  ```

## 其它



# [容器](https://docs.docker.com/reference/cli/docker/container/)

## 容器基础

- **基础命令**

  ```bash
  # 查看容器
  docker ps [-a] # -a表示全部，包含未运行
  # 创建容器
  docker create IMAGE
  # 启动容器
  docker start CONTAINER_NAME
  # 创建并启动容器
  docker run [-d] [-it] --name CONTAINER_NAME IMAGE
  # 重启容器
  docker restart CONTAINER_NAME
  # 停止容器
  docker stop CONTAINER_NAME
  # 删除容器
  docker rm CONTAINER_NAME
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

- **[-d (--detach)](https://docs.docker.com/reference/cli/docker/container/run/#detach)**：在后台运行容器并打印容器 ID，不占用终端

- [**-e (--env ; --env-file)**](https://docs.docker.com/reference/cli/docker/container/run/#env)：设置环境变量

- [**--entrypoint /bin/sh**](https://docs.docker.com/compose/compose-file/05-services/#entrypoint)：设置容器的入口点，后面的值 `/bin/sh` 表示启动容器后直接进入 Shell 环境。

- [**-f (--force)**](https://docs.docker.com/reference/cli/docker/container/rm/#force)：强制删除运行中的容器

- **-it**：(-i 和 -t 的组合)

  - [**-t (--tty)**](https://docs.docker.com/reference/cli/docker/container/run/#tty)：分配一个伪终端 (TTY) 给容器，这样可以在容器中执行交互式的命令
  - [**-i (--interactive)**](https://docs.docker.com/reference/cli/docker/container/run/#interactive)：让容器的标准输入保持打开，以便我们可以与容器进行交互

- [**--name**](https://docs.docker.com/reference/cli/docker/container/run/#name)：命名容器

- [**-p (--publish)**](https://docs.docker.com/reference/cli/docker/container/run/#publish)：端口映射

  ```bash
  -p [HOST_PORT]:[CONTAINER_PORT]
  #eg
  -p 80:8080
  ```

- [**`-t <IMAGE_NAME>:<TAG>`**](https://docs.docker.com/reference/cli/docker/image/build/#tag)：命名镜像（-t / --tag），标签可省略，可一次使用多个 `-t`

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

## 指令说明

- **ENTRYPOINT**：设置容器的入口点

## 手动训练

- 这个训练用于手动模拟 Dockerfile 文件创建一个容器化应用，这是一个 Web Server

- [从 Github 下载样本文件到 Linux 系统](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/da3e2c22c727e3b6d72d4eea04c19335db0727cb/quickstarts/hello-app) 

  - 下载

    ```bash
    curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/main/quickstarts/hello-app/main.go -O https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/main/quickstarts/hello-app/Dockerfile
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
            // register hello function to handle all requests
            mux := http.NewServeMux()
            mux.HandleFunc("/", hello)
    
            // use PORT environment variable, or default to 8080
            port := os.Getenv("PORT")
            if port == "" {
                    port = "8080"
            }
    
            // start the web server on port and accept requests
            log.Printf("Server listening on port %s", port)
            log.Fatal(http.ListenAndServe(":"+port, mux))
    }
    
    // hello responds to the request with a plain-text "Hello, world" message.
    func hello(w http.ResponseWriter, r *http.Request) {
            log.Printf("Serving request: %s", r.URL.Path)
            host, _ := os.Hostname()
            fmt.Fprintf(w, "Hello, world!\n")
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
    
    # 原文件不是这个image，导致容器无法启动
    FROM debian
    WORKDIR /
    COPY --from=builder /hello-app /hello-app
    ENV PORT 8080
    
    # 原文件没有这句，导致找不到nonroot用户，容器无法启动
    RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
    
    USER nonroot:nonroot
    CMD ["/hello-app"]
    ```

- 模拟过程

  ```bash
  # 创建编译环境容器
  docker run -d -it --name builder golang:1.21.0
  # 进入编译环境容器
  docker exec -it builder /bin/sh
  # 创建工作目录app
  cd /
  mkdir app
  ## 模块化
  go mod init hello-app
  exit
  
  # 复制main.go至容器内的工作目录app
  docker cp *.go builder:/app
  # 进入编译环境容器
  docker exec -it builder bash   
  cd /app
  # 编译你的 Go 应用程序为静态 Linux 可执行文件。然后，你将编译好的可执行文件保存为 /hello-app。
  CGO_ENABLED=0 GOOS=linux go build -o /hello-app
  exit  
  
  # 创建生产环境：通过将应用程序从 builder 镜像中复制到这个镜像中，并设置相应的运行时配置，最终生成的镜像将是一个精简的、只包含应用程序和运行时环境的最小化镜像，从而降低了攻击面和维护成本。
  # 由于不允许运行，我使用了一个新image
  docker container run -d -it -p 80:8080 --name runner debian
  # 从编译环境中复制应用程序 hello-ap 到生产环境
  docker cp builder:/hello-app /hello
  docker cp /hello/hello-app runner:/hello-app
    
  # 进入生产环境
  docker exec -it runner bash
  # 暴露生产环境的8080端口
  export PORT=8080
  
  # 添加nonroot用户
  adduser --disabled-password --gecos "" nonroot
  # 运行应用程序
  /hello-app
  ```

- 接下来与给定的 Dockerfile 无关，旨在基于此练习中的 runner 容器（无需运行），记录 commit 添加 `-c` 选项的用法

  - 从 container 创建 image

    为 commit 添加 `-c 'ENTRYPOINT ["/hello-app"]'` 选项，达到启动容器即可直接访问应用，而无需进入容器启动应用

    ```bash
    docker commit -c 'ENTRYPOINT ["/hello-app"]' runner dockerfile-manually
    ```

  - 从 image 创建并运行 container

    ```bash
    docker run -d -it -p 80:8080 --name hello-app dockerfile-manually
    ```

  - 访问应用

    ```bash
    # 在容器内访问应用，新建终端
    curl http://127.0.0.1:8080
    # 在Linux中访问应用
    curl http://127.0.0.1:80
    ```

# 其它



