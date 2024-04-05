# Aircraft Battle

- 这是一个基于 Python 的游戏，使用 pygame 模块开发

- 项目文件存储于 Git 仓库

  ```
  # 老师操作步骤
  
  1.构建整体结构
  
  2.main中创建窗口对象
  
  3.初始化定义属性
  
  初始化Player
  初始化PlayerBullet
  初始化Enemy
  初始化EnemyrBullet
  
  4.创建对象
  
  创建background
  创建player
  创建enemy
  
  5.显示对象
  
  死循环while
  背景图片
  显示对象：调display
  未写敌机开火和Key_ctrol
  
  5.1定义display
  玩家-不含子弹
  敌机-不含子弹
  
  6.键盘控制
  编写键盘控制（只有退出）
  将Key_ctrol填入main()
  
  7.定义敌机move和fire
  敌机move
  添加至main()
  敌机子弹和fire
  ```

  ```python
  import time  # 控制刷新频率
  import pygame
  from pygame.locals import *  # 检测事件，如监控键盘按键
  import sys  # 用来退出游戏
  import random  # 控制子弹随机发射
  
  
  # 玩家类：
  # 属性：显示窗口、位置、图片、子弹列表、移动状态
  # 方法：显示、移动、开火
  class Player():
      def __init__(self, screen):  # 将main()中的screen传入
          self.screen = screen  # 将一个窗口对象作为了属性值，表示玩家对象显示的窗口
          # 等号左侧的screen为类的形参，右侧的为实参，右侧为main()中定义的screen
          self.x = 150  # 玩家初始位置
          self.y = 500
          self.img = pygame.image.load(r"feiji/hero1.png")  # 玩家图片
          self.bulletList = []  # 玩家子弹列表
          self.moveLeftState = 0  # 0不移动  1移动
          self.moveRightState = 0  # 0不移动  1移动
  
      def display(self):
          # 当前对象所在的screen属性下，调blit函数
          self.screen.blit(self.img, (self.x, self.y))  # 将玩家显示到窗口
          for b in self.bulletList:  # 创建子弹，并在子弹列表中遍历
              b.display()  # 将玩家子弹显示到窗口
              b.move()  # 将玩家子弹移动状态显示到窗口
              if b.y <= 0:
                  self.bulletList.remove(b)  # 在子弹列表中移除b
  
      def move(self):
          if self.moveLeftState == 1 and self.x > -30:
              self.x -= 5
          if self.moveRightState == 1 and self.x < 330:
              self.x += 5
  
      def fire(self):
          b = PlayerBullet(self.screen, self.x, self.y)
          self.bulletList.append(b)
  
  
  # 玩家子弹类：
  # 属性：显示窗口、位置、图片
  # 方法：显示、移动
  class PlayerBullet():
      def __init__(self, screen, x, y):  # xy为玩家位置，传入给玩家子弹
          self.screen = screen
          self.x = x + 40  # 玩家子弹初始位置，需要跟随玩家飞机
          self.y = y - 20
          self.img = pygame.image.load(r"feiji/bullet.png")
  
      def display(self):
          self.screen.blit(self.img, (self.x, self.y))
  
      def move(self):
          self.y -= 20
  
  
  # 敌机类
  # 属性：显示窗口、位置、图片、子弹列表、移动状态
  # 方法：显示、移动、开火
  class Enemy():
      def __init__(self, screen):
          self.screen = screen
          self.x = 0  # 敌机初始位置
          self.y = 0
          self.img = pygame.image.load(r"feiji/enemy0.png")
          self.bulletList = []
          self.moveState = 1
  
      def display(self):
          # 当前对象所在的screen属性下，调blit函数
          self.screen.blit(self.img, (self.x, self.y))
          for b in self.bulletList:
              b.display()
              b.move()
              if b.y >= 600:
                  self.bulletList.remove(b)
  
      def move(self):
          if self.moveState == 1:
              self.x += 5
          elif self.moveState == 0:
              self.x -= 5
          if self.x < -20:
              self.moveState = 1
          if self.x > 280:
              self.moveState = 0
  
      def fire(self):
          b = EnemyBullet(self.screen, self.x, self.y)
          self.bulletList.append(b)
  
  
  # 敌机子弹类
  # 属性：显示窗口、位置、图片
  # 方法：显示、移动
  class EnemyBullet():
      def __init__(self, screen, x, y):  # xy为敌机位置，传入给敌机子弹
          self.screen = screen
          self.x = x + 20  # 敌机子弹初始位置，需要跟随敌机飞机
          self.y = y + 30
          self.img = pygame.image.load(r"feiji/bullet2.png")
  
      def display(self):
          self.screen.blit(self.img, (self.x, self.y))
  
      def move(self):
          self.y += 20
  
  
  # 捕捉用户操作
  def key_control(player):  # 传入玩家对象，只控制玩家
      for event in pygame.event.get():
          if event.type == QUIT:
              print("正在退出....")
              sys.exit(0)
          elif event.type == KEYDOWN:  # 按下键盘
              if event.key == K_LEFT:
                  print("玩家向左！")
                  player.moveLeftState = 1
              if event.key == K_RIGHT:
                  print("玩家向右！")
                  player.moveRightState = 1
              if event.key == K_SPACE:
                  print("玩家开火！")
                  player.fire()
          elif event.type == KEYUP:  # 松开键盘
              if event.key == K_LEFT:
                  player.moveLeftState = 0
              if event.key == K_RIGHT:
                  player.moveRightState = 0
  
  
  # main方法
  class main():
      # 创建对象
      screen = pygame.display.set_mode((300, 600))  # 创建窗口
      background = pygame.image.load(r"feiji/background.png")  # 创建背景
      player = Player(screen)  # 创建玩家，并将screen属性传入玩家
      enemy = Enemy(screen)  # 创建敌军，并将screen属性传入敌军
  
      while 1 == 1:  # 在循环中显示所有对象并刷新，以实现对象的变化
          screen.blit(background, (0, 0))  # 将背景添加到屏幕，即显示背景
          player.display()  # 显示玩家，因为玩家还要显示其它操作。所以玩家的显示写在display中
          enemy.display()  # 显示敌机
          player.move()  # 玩家移动
          enemy.move()  # 敌机移动
  
          # 敌机随机开火
          r = random.randint(1, 10)
          if r == 1:
              enemy.fire()
  
          # 捕捉玩家操作
          key_control(player)
  
          pygame.display.update()  # 刷新窗口
          time.sleep(0.05)  # 休眠0.05秒，减少内存消耗
  
  
  # ---------------------------
  if __name__ == '__main__':
      main()
  ```

# ATM

## 项目概述

- 这是一个 Python 练习，旨在练习控制结构；
- 模拟3张银行卡，1001，1002，1003，分别设置密码和余额（使用列表嵌套字典的方式）；
- 提示用户输入银行卡和密码，遍历每张卡的信息验证是否成功；
- 如果用户输入正确
  - 提示让用户选择取款，存款还是退出，并提示余额多少；
- 输入错误
  - 重新输入卡号密码；
  - 错误 3 次即锁卡，程序结束；

## 具体步骤

- 脚本

  ```python
  card1 = {"姓名": "张三", "卡号": "111", "密码": "111", "余额": 10000}
  card2 = {"姓名": "李四", "卡号": "222", "密码": "222", "余额": 20000}
  card3 = {"姓名": "王五", "卡号": "333", "密码": "333", "余额": 30000}
  cardslist = [card1, card2, card3]
  count = 0  # 记录输入错误的次数
  msg = 0  # 记录登录状态 0失败 1成功！
  
  # 登录业务
  while 1 == 1:  # 输入账号和密码的无限循环
      cnum = input("请输入卡号：")
      cpwd = input("请输入密码：")
      for card in cardslist:
          if cnum == card["卡号"] and cpwd == card["密码"]:
              msg = 1  # 设定登录成功！
              count = 0  # 当验证成功时，错误次数清零
              print("恭喜你", card["姓名"], "登录成功！")
      if msg == 0:  # 设定登录失败！
          count += 1  # 失败次数加1
          if count < 3:
              print("验证失败！您已连续", count, "次输入错误，还有", 3 - count, "次机会，请重新输入：")
              continue
          elif count == 3:
              print("您已连续3次输入错误，银行卡已被锁定！")
              break
  
      # 银行业务
      while 2 == 2:  # 选择业务的无限循环
          choice = int(input("请输入要办理的业务（1.存款 2.取款 3.退出）："))
          if choice == 1:
              money1 = float(input("请输入存款金额："))
              for card in cardslist:
                  if card["卡号"] == cnum:
                      card["余额"] += money1
                      print("存款成功！", "存入", money1, "元！", "余额", card["余额"], "元！")
          elif choice == 2:
              money2 = float(input("请输入取款金额："))
              for card in cardslist:
                  if card["卡号"] == cnum:
                      card["余额"] -= money2
                      print("取款成功！", "取出", money2, "元！", "余额", card["余额"], "元！")
          elif choice == 3:
              print("已退出！")
              break
          else:
              print("没有此业务，请重新选择：")
              continue
  ```

# Argo CD Git

## 项目概述

- **项目来源**：[ YouTube 博主 TechWorld with Nana](https://www.youtube.com/watch?v=MeU5_k9ssrs)
- **文件来源**：[使用项目 Student Spring Boot React Full Stack 的 jerrybaijy/student-springboot-react-frontend:v1.0](https://hub.docker.com/repository/docker/jerrybaijy/student-springboot-react-frontend/general)
- **概述**：此项目旨在实现通过 Argo CD 以 Git 方式（区别于 Helm 方式）在集群中部署一个应用
- **存储**：代码存储在 Git 托管平台

## 具体步骤

1. 集群已运行，Argo CD 已安装。

2. UI 界面创建 Git 仓库 argocd-git，clone 至本地

3. argocd-git 根目录创建 dev 目录

4. dev 目录创建 deployment.yaml

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: argocd-git
   spec:
     selector:
       matchLabels:
         app: argocd-git
     replicas: 1
     template:
       metadata:
         labels:
           app: argocd-git
       spec:
         containers:
           - name: argocd-git
             image: jerrybaijy/student-springboot-react-frontend:v1.0
             ports:
               - containerPort: 8080
             env:
               - name: PORT
                 value: "8080"
             resources:
               requests:
                 memory: "1Gi"
                 cpu: "500m"
                 ephemeral-storage: "1Gi"
               limits:
                 memory: "1Gi"
                 cpu: "500m"
                 ephemeral-storage: "1Gi"
   ```

5. dev 目录创建 service.yaml

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: argocd-git
   spec:
     selector:
       app: argocd-git
     type: LoadBalancer # 如本地访问服务类型为 ClusterIP
     ports:
       - port: 80
         targetPort: 8080
   ```

6. argocd-git 根目录创建 application.yaml

   ```yaml
   apiVersion: argoproj.io/v1alpha1
   kind: Application
   metadata:
     name: argocd-git
     namespace: argocd
   
   spec:
     project: default
     source:
       repoURL: https://gitlab.com/jerrybai/argocd-git.git
       targetRevision: HEAD
       path: dev
     
     destination:
       server: https://kubernetes.default.svc
       namespace: argocd-git
   
     syncPolicy:
       syncOptions:
         - CreateNamespace=true
       automated:
         selfHeal: true
         prune: true
   ```

7. 部署应用

   ```
   kubectl apply -f application.yaml
   ```

8. 查看 IP 即可访问应用（如有需要可进行端口转发）

   ```bash
   kubectl get svc -n argocd-git
   ```

## 未验证

- **以下内容为 Nana 视频提及的信息，还未验证**
- 等价产品：Flux CD

流程

- 开发人员将代码推送至 GitHub
- A 自动构建 image 并推送至 Dockerhub
- 最后更新 K8S yaml 文件

Nana 说最好将代码源文件和 yaml 文件分别存储，以利于更改代码或部署时，不必检查另一方，最终有单独的 CI 和 CD

yaml 文件、helm 图表、K8S 清单、自定义文件或其它模板文件，所有都会自动转换为纯 K8S yaml 文件



A 不仅监视存储库更改，还会监视集群中的更改，双方任意一个改变，另一方将自动更改

一个 A 可以同时配置多个集群

# Argo CD Helm

## 项目概述

- **项目来源**：学完 Helm Chart 以后，自己基于项目 Argo CD Git，以 Helm 方式在集群中部署一个应用
- **文件来源**：[使用项目 Student Spring Boot React Full Stack 的 jerrybaijy/student-springboot-react-frontend:v1.0](https://hub.docker.com/repository/docker/jerrybaijy/student-springboot-react-frontend/general)
- **概述**：此项目旨在实现通过 Argo CD 以 Helm 方式（区别于 Git 方式）在集群中部署一个应用
- **存储**：代码存储在 Git 托管平台

## 具体步骤

1. 集群已运行，Argo CD 已安装。

2. UI 界面创建 Git 仓库 argocd-git-helm，clone 至本地

3. 创建 argocd-helm-chart.0.1.0.tgz。

   - deployment.yaml

     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: {{ include "argocd-helm-chart.fullname" . }}
       labels:
         {{- include "argocd-helm-chart.labels" . | nindent 4 }}
     spec:
       {{- if not .Values.autoscaling.enabled }}
       replicas: {{ .Values.replicaCount }}
       {{- end }}
       selector:
         matchLabels:
           {{- include "argocd-helm-chart.selectorLabels" . | nindent 6 }}
       template:
         metadata:
           {{- with .Values.podAnnotations }}
           annotations:
             {{- toYaml . | nindent 8 }}
           {{- end }}
           labels:
             {{- include "argocd-helm-chart.labels" . | nindent 8 }}
             {{- with .Values.podLabels }}
             {{- toYaml . | nindent 8 }}
             {{- end }}
         spec:
           {{- with .Values.imagePullSecrets }}
           imagePullSecrets:
             {{- toYaml . | nindent 8 }}
           {{- end }}
           serviceAccountName: {{ include "argocd-helm-chart.serviceAccountName" . }}
           securityContext:
             {{- toYaml .Values.podSecurityContext | nindent 8 }}
           containers:
             - name: {{ .Chart.Name }}
               securityContext:
                 {{- toYaml .Values.securityContext | nindent 12 }}
               image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
               imagePullPolicy: {{ .Values.image.pullPolicy }}
               ports:
                 - name: http
                   containerPort: {{ .Values.service.targetPort }}
                   protocol: TCP
               livenessProbe:
                 {{- toYaml .Values.livenessProbe | nindent 12 }}
               readinessProbe:
                 {{- toYaml .Values.readinessProbe | nindent 12 }}
               resources:
                 {{- toYaml .Values.resources | nindent 12 }}
               {{- with .Values.volumeMounts }}
               volumeMounts:
                 {{- toYaml . | nindent 12 }}
               {{- end }}
           {{- with .Values.volumes }}
           volumes:
             {{- toYaml . | nindent 8 }}
           {{- end }}
           {{- with .Values.nodeSelector }}
           nodeSelector:
             {{- toYaml . | nindent 8 }}
           {{- end }}
           {{- with .Values.affinity }}
           affinity:
             {{- toYaml . | nindent 8 }}
           {{- end }}
           {{- with .Values.tolerations }}
           tolerations:
             {{- toYaml . | nindent 8 }}
           {{- end }}
     ```

   - service.yaml

     ```yaml
     apiVersion: v1
     kind: Service
     metadata:
       name: {{ include "argocd-helm-chart.fullname" . }}
       labels:
         {{- include "argocd-helm-chart.labels" . | nindent 4 }}
     spec:
       type: {{ .Values.service.type }}
       ports:
         - port: {{ .Values.service.port }}
           targetPort: {{ .Values.service.targetPort }}
           protocol: TCP
           name: http
       selector:
         {{- include "argocd-helm-chart.selectorLabels" . | nindent 4 }}
     ```

   - values.yaml

     ```yaml
     replicaCount: 1
     image:
       repository: jerrybaijy/student-springboot-react-frontend
       pullPolicy: IfNotPresent
       tag: "v1.0"
     imagePullSecrets: []
     nameOverride: ""
     fullnameOverride: ""
     serviceAccount:
       create: true
       automount: true
       annotations: {}
       name: ""
     podAnnotations: {}
     podLabels: {}
     podSecurityContext: {}
     securityContext: {}
     
     service:
       type: LoadBalancer
       port: 80
       targetPort: 8080
     
     ingress:
       enabled: false
       className: ""
       annotations: {}
       hosts:
         - host: chart-example.local
           paths:
             - path: /
               pathType: ImplementationSpecific
       tls: []
     resources: {}
     livenessProbe:
       httpGet:
         path: /
         port: http
     readinessProbe:
       httpGet:
         path: /
         port: http
     autoscaling:
       enabled: false
       minReplicas: 1
       maxReplicas: 100
       targetCPUUtilizationPercentage: 80
     volumes: []
     volumeMounts: []
     nodeSelector: {}
     tolerations: []
     affinity: {}
     ```

4. 建立远程 Helm 仓库

5. 创建 Argo CD 的 application.yaml

   ```yaml
   apiVersion: argoproj.io/v1alpha1
   kind: Application
   metadata:
     name: argocd-helm
     namespace: argocd
   
   spec:
     project: default
     source:
       repoURL: https://jerrybaijy.github.io/argocd-helm/
       targetRevision: 0.1.0
       chart: argocd-helm-chart
       helm:
         valueFiles:
           - values.yaml
     destination:
       server: https://kubernetes.default.svc
       namespace: argocd-helm
   
     syncPolicy:
       syncOptions:
         - CreateNamespace=true
       automated:
         selfHeal: true
         prune: true
   ```

6. 部署应用

   ```bash
   kubectl apply -f application.yaml
   ```

7. 查看 IP 即可访问应用（如有需要可进行端口转发）

   ```bash
   kubectl get svc -n argocd-helm
   ```

## 方法二

1. This method deploy a App manually through a command, including the options instead of YAML file `application.yaml`

2. This method is unverified

3. Creat a new GitHub  repository and clone it to local

4. Create a Helm chart in the local repo and config the YAML file

5. Use the Argo CLI to deploy your chart into your Kubernetes cluster

   ```bash
   argocd app create $DEPLOYMENT_NAME \
   	--repo https://github.com/$USERNAME/$REPO.git \
   	--path $PATH \
   	--dest-server https://kubernetes.default.svc \
   	--dest-namespace $NAMESPACE \
   	--sync-option CreateNamespace=true \
   	--parameter namespace=$NAMESPACE \
   ```

6. Config others ...

# Dockerfile Build Image

## 项目概述

- **来源**：[GoogleCloudPlatform/kubernetes-engine-samples/quickstarts/hello-app/](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/da3e2c22c727e3b6d72d4eea04c19335db0727cb/quickstarts/hello-app)
- **概述**：这是一个简单的 Go 语言 Web Server 应用项目，旨在实现在本地通过 Dockerfile 创建镜像。
- **存储**
  - 代码存储在 Git 托管平台
  - 镜像存储在 DockerHub

## 创建过程

1. 创建 web-server.go 文件

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

2. 创建 Dockerfile 文件

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

3. 创建镜像

   ```bash
   docker build -t dockerfile-build-image .
   ```

4. 运行容器

   ```bash
   docker run -d -p 80:8080 --name test dockerfile-build-image:latest
   ```

5. 本地访问应用：http://127.0.0.1:80

# GitLab CI Image

## 项目概述

- **来源**：[GoogleCloudPlatform/kubernetes-engine-samples/quickstarts/hello-app/](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/da3e2c22c727e3b6d72d4eea04c19335db0727cb/quickstarts/hello-app)
- **文件**：web-server.go 和 Dockerfile 从 Dockerfile Build Image 项目复制
- **概述**：这是一个简单的 Go 语言 Web Server 应用项目，旨在实现通过 GitLab CI 创建镜像。
- **存储**
  - 代码存储在 Git 托管平台
  - 镜像存储在 DockerHub

## 创建过程

1. 创建 web-server.go 文件

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

2. 创建 Dockerfile 文件

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

3. 创建 .gitlab-ci.yml 文件

   ```yaml
   variables:
     IMAGE_NAME: jerrybaijy/gitlab-ci-image
     IMAGE_TAG: v1.0
   
   stages: 
     - build
   
   build_image:
     stage: build
     image: docker:20.10.20
     services:
       - docker:20.10.20-dind
     variables:
       DOCKER_TLS_CERTDIR: "/certs"
     before_script:
       - docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
     script:
       - docker build -t $IMAGE_NAME:$IMAGE_TAG .
       - docker push $IMAGE_NAME:$IMAGE_TAG
   ```

4. 推送至 GitLab

   - 项目文件推送至远程仓库
   - GitLab 在 Pipeline 中自动生成 Image 并推送至 DockerHub

# Student Spring Boot React Full Stack

![image](assets/image.png)

## 项目概述

- **来源**：[YouTube 博主 Arjun Full Stack web application using Spring Boot and React | REST API | MySQL | React Hooks](https://www.youtube.com/watch?v=O_XL9oQ1_To)
- **项目概述**：这是一个全栈 Web 应用项目，主要功能是网页端与数据库的数据交互。
- **前端**：使用 Java Script 的 React 框架搭建
- **后端**：使用 Java 的 Spring Boot 框架搭建
- **数据库**：使用 XAMPP 集成的 MySQL
- **代码存储**：前后端和数据库以三个分项目形式分别存储在托管平台
  - student-springboot-react-frontend
  - student-springboot-react-backend
  - student-springboot-react-database


## 后端

### 后端环境搭建

- **框架**：Spring Boot
- **语言**：Java
- **环境依赖**：JDK
- **IDE**：IDEA

### 创建后端项目

- 完成  Spring Boot 环境搭建，详见  Spring Boot

- 项目依赖：Spring Web, MySQL Driver, Spring Data JPA

- IDEA 打开项目文件夹


### 创建包和类

- 创建 package `model`
  - 创建 class `Student`
- 创建 package `respository`
  - 创建 class - Interface `StudentReporitory`（数据库接口）
- 创建 package `controller`（用于映射所有 http 方法）
  - 创建 class `StudentCtroller`
- 创建 package `service`
  - 创建 class - Interfaces `StudentService` （服务接口）
  - 创建 class `StudentServiceImpl` （服务实现）

### model

- 类和对象：model / Student.java

  ```java
  package com.jerrycodes.studentsystem.model;
  
  import com.jerrycodes.studentsystem.repository.StudentRepository;
  import jakarta.persistence.*;
  
  @Entity
  public class Student {
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      // 类的属性
      private int id;
      private String name;
      private String address;
  
  
      // 类的实例对象：Alt + Insert - Constructor - int.int
      public Student() {}
  
      // 为删除学生而写
      public Student(String name, String address) {
          this.name = name;
          this.address = address;
      }
  
      // 类的方法：Alt + Insert - Getter and Setter - int.int, name:String, address:String
      public int getId() {
          return id;
      }
      public void setId(int id) {
          this.id = id;
      }
      public String getName() {
          return name;
      }
      public void setName(String name) {
          this.name = name;
      }
      public String getAddress() {
          return address;
      }
      public void setAddress(String address) {
          this.address = address;
      }
      // 删除学生信息
      public void delete(EntityManager entityManager) {
          entityManager.getTransaction().begin();
          entityManager.remove(this);
          entityManager.getTransaction().commit();
      }
      // 修改学生信息
      public void update(String newName, String newAddress) {
          if (newName != null) {
              this.name = newName;
          }
          if (newAddress != null) {
              this.address = newAddress;
          }
      }
  }
  ```


### repository

- 数据库接口：repository / StudentRrpository.java

  ```java
  package com.jerrycodes.studentsystem.repository;
  
  import com.jerrycodes.studentsystem.model.Student;
  import org.springframework.data.jpa.repository.JpaRepository;
  import org.springframework.stereotype.Repository;
  
  @Repository
  public interface StudentRepository extends JpaRepository<Student, Integer> {
  }
  ```

### service

- 服务接口：service / StudentService.java

  ```java
  package com.jerrycodes.studentsystem.service;
  
  import com.jerrycodes.studentsystem.model.Student;
  
  import java.util.List;
  
  public interface StudentService {
      public Student saveStudent(Student student);
      public List<Student> getAllStudents();
      public void deleteStudent(int studentId);
      public void updateStudent(int studentId, String name, String address);
  }
  ```

- 服务实现：service / StudentServicelmpl.java

  ```java
  package com.jerrycodes.studentsystem.service;
  
  import com.jerrycodes.studentsystem.model.Student;
  import com.jerrycodes.studentsystem.repository.StudentRepository;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Service;
  import com.jerrycodes.studentsystem.exception.StudentNotFoundException;
  
  import java.util.List;
  
  @Service
  public class StudentServicelmpl implements StudentService{
      // 连接数据库
      @Autowired
      private StudentRepository studentRepository;
  
      // 保存，Alt + Insert - Override Methods... - SaveStudent(student:Student):Student
      @Override
      public Student saveStudent(Student student) {
          return studentRepository.save(student);
      }
  
      // 获取：Alt + Insert - Override Methods... - getALLStudents():List<Student>
      @Override
      public List<Student> getAllStudents() {
          return studentRepository.findAll();
      }
  
      @Override
      public void deleteStudent(int studentId) {
          studentRepository.deleteById(studentId);
      }
      @Override
      public void updateStudent(int studentId, String name, String address) {
          Student studentToUpdate = studentRepository.findById(studentId).orElse(null);
          if (studentToUpdate != null) {
              studentToUpdate.setName(name);
              studentToUpdate.setAddress(address);
              studentRepository.save(studentToUpdate);
          } else {
              throw new StudentNotFoundException("Student with ID " + studentId + " not found.");
          }
      }
  }
  ```

### controller

- 控制器：controller / StudentController.java

  ```java
  package com.jerrycodes.studentsystem.controller;
  
  import com.jerrycodes.studentsystem.model.Student;
  import com.jerrycodes.studentsystem.service.StudentService;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.web.bind.annotation.*;
  
  import java.util.List;
  
  
  @RestController
  @RequestMapping("/student")
  @CrossOrigin
  public class StudentController {
      @Autowired
      private StudentService studentService;
  
      @PostMapping("/add")
      public String add(@RequestBody Student student){
          studentService.saveStudent(student);
          return "New student is added";
      }
  
      @GetMapping("/getAll")
      public List<Student> getAllStudents(){
          return studentService.getAllStudents();
      }
  
      @DeleteMapping("/delete/{studentId}")
      public String delete(@PathVariable int studentId){
          studentService.deleteStudent(studentId);
          return "Student with ID " + studentId + " is deleted";
      }
      @PutMapping("/update/{studentId}")
      public String update(@PathVariable int studentId, @RequestBody Student updatedStudent) {
          studentService.updateStudent(studentId, updatedStudent.getName(), updatedStudent.getAddress());
          return "Student with ID " + studentId + " is updated";
      }
  }
  ```

### 本地数据库

- **工具**：使用 XAMPP 集成的 Apache MySQL Tomcat 创建数据库
- 启动 XAMPP，创建数据库 fullstack

### 连接数据库

- 提前完成数据库搭建

- 连接数据库：resources / application.properties

  ```properties
  # configuration
  spring.jpa.hibernate.ddl-auto=update
  spring.datasource.url=jdbc:mysql://localhost:3306/fullstack
  spring.datasource.username=jerry
  spring.datasource.password=123456
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  ```

  删掉了原文件自动生成的一句代码：`spring.application.name=studentsystem`

- 此时转到 StudentsystemApplication.java 文件即可运行应用，验证数据库启动成功

- 在数据库 Admin 页面可以看到已经创建了 student 数据表

### 调试后端

- 启动 APP 后端
- 使用 Postman 模拟前端浏览器与后端交互
- 调试通过即可转向前端开发

### 构建项目

- 在项目的根目录中运行 Maven 命令来构建项目，将生成的可执行 JAR 文件 `studentsystem-0.0.1-SNAPSHOT.jar` 复制到项目根目录

  ```bash
  mvn clean package -DskipTests
  ```

### 生成 Image

- 使用 GitLab Pipeline 生成 Image

- .gitlab-ci.yml

  ```yaml
  variables:
    IMAGE_NAME: jerrybaijy/student-springboot-react-backend
    IMAGE_TAG: v1.0
  
  stages: 
    - build
  
  build_image:
    stage: build
    image: docker:20.10.20
    services:
      - docker:20.10.20-dind
    variables:
      DOCKER_TLS_CERTDIR: "/certs"
    before_script:
      - docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
    script:
      - docker build -t $IMAGE_NAME:$IMAGE_TAG .
      - docker push $IMAGE_NAME:$IMAGE_TAG
  ```

- Dockerfile

  ```bash
  FROM openjdk:17.0.1-jdk-slim
  WORKDIR /app
  COPY studentsystem-0.0.1-SNAPSHOT.jar app.jar
  EXPOSE 8080
  CMD ["java", "-jar", "app.jar"]
  ```

### 部署应用

1. 使用 Argo CD 在集群中部署

2. application.yaml

   ```yaml
   apiVersion: argoproj.io/v1alpha1
   kind: Application
   metadata:
     name: student-springboot-react-backend
     namespace: argocd
   
   spec:
     project: default
     source:
       repoURL: https://gitlab.com/jerrybai/student-springboot-react-backend.git
       targetRevision: HEAD
       path: dev
     
     destination:
       server: https://kubernetes.default.svc
       namespace: student-springboot-react-backend
   
     syncPolicy:
       syncOptions:
         - CreateNamespace=true
       automated:
         selfHeal: true
         prune: true
   ```

3. deploymnet.yaml

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: student-springboot-react-backend
   spec:
     selector:
       matchLabels:
         app: student-springboot-react-backend
     replicas: 1
     template:
       metadata:
         labels:
           app: student-springboot-react-backend
       spec:
         containers:
           - name: student-springboot-react-backend
             image: jerrybaijy/student-springboot-react-backend:v1.0
             ports:
               - containerPort: 8080
             env:
               - name: PORT
                 value: "8080"
             resources:
               requests:
                 memory: "1Gi"
                 cpu: "500m"
                 ephemeral-storage: "1Gi"
               limits:
                 memory: "1Gi"
                 cpu: "500m"
                 ephemeral-storage: "1Gi"
   ```

4. service.yaml

   ```bash
   apiVersion: v1
   kind: Service
   metadata:
     name: student-springboot-react-backend
   spec:
     selector:
       app: student-springboot-react-backend
     type: ClusterIP
     ports:
       - port: 80
         targetPort: 8080
   ```

## 前端

### 前端环境搭建

- **框架**：React
- **语言**：HTML, CSS, Java Script, JavaScript XML, React Hooks
- **环境依赖**：Node.js
- **IDE**：VS Code, IDEA
- **其它工具**
	- **Postman**：模拟浏览器
	- **Material UI**：React 组件依赖

### 具体步骤

1. 创建 React 项目，具体方法详见 React

   1. 创建 React APP
   2. 安装 Material-UI 和 Material Icons
   3. 创建组件文件 `Appbar.js` 和  `Student.js`

2. 创建组件 `Appbar.js`

   ```js
   import * as React from 'react';
   import AppBar from '@mui/material/AppBar';
   import Box from '@mui/material/Box';
   import Toolbar from '@mui/material/Toolbar';
   import Typography from '@mui/material/Typography';
   import Button from '@mui/material/Button';
   import IconButton from '@mui/material/IconButton';
   import MenuIcon from '@mui/icons-material/Menu';
   
   // 此处的 Appbar 即主程序文件 App.js 中的 <Appbar />
   export default function Appbar() {
     return (
       <Box sx={{ flexGrow: 1 }}>
         <AppBar position="static">
           <Toolbar>
             <IconButton
               size="large"
               edge="start"
               color="inherit"
               aria-label="menu"
               sx={{ mr: 2 }}
             >
               <MenuIcon />
             </IconButton>
             <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
               Spring Boot React Full Stack
             </Typography>
             <Button color="inherit">Login</Button>
           </Toolbar>
         </AppBar>
       </Box>
     );
   }
   ```

3. 创建组件  `Student.js`

   ```js
   import * as React from 'react';
   import Box from '@mui/material/Box';
   import TextField from '@mui/material/TextField';
   import { Button, Container, Paper } from '@mui/material';
   
   // 此处的 Student 即主程序文件 App.js 中的 <Student />
   export default function Student() {
     const paperStyle = { padding: '50px 20px', width: 600, margin: '20px auto' }
   
     const [students, setStudents] = React.useState([])
     const [name, setName] = React.useState('')
     const [address, setAddress] = React.useState('')
   
     // 定义 getAll
     const fetchStudents = () => {
       fetch("http://localhost:8080/student/getAll")
         .then(res => res.json())
         .then((result) => {
           setStudents(result);
         })
     }
   
     // 在组件挂载时获取学生信息
     React.useEffect(fetchStudents, [])
   
     // 定义 add
     const handleClick = (e) => {
       e.preventDefault()
       const student = { name, address }
       console.log(student)
       fetch("http://localhost:8080/student/add", {
         method: "POST",
         headers: { "Content-Type": "application/json" },
         body: JSON.stringify(student)
       }).then(() => {
         console.log("New Student added")
         fetchStudents();
       })
     }
   
     // 定义 delete
     const handleDelete = (studentId) => {
       fetch(`http://localhost:8080/student/delete/${studentId}`, {
         method: "DELETE"
       }).then(() => {
         console.log(`Student with ID ${studentId} deleted`);
         // 删除学生后更新页面以显示删除后的学生信息
         setStudents(students.filter(student => student.id !== studentId));
       });
     }
   
     // 定义 update
     const handleUpdate = (studentId) => {
       const updatedName = name;
       const updatedAddress = address;
       const updatedStudent = { name: updatedName, address: updatedAddress }
       fetch(`http://localhost:8080/student/update/${studentId}`, {
         method: "PUT",
         headers: { "Content-Type": "application/json" },
         body: JSON.stringify(updatedStudent)
       }).then(() => {
         console.log(`Student with ID ${studentId} updated`);
         // 更新学生信息后更新页面以显示最新的学生信息
         fetchStudents();
       });
     }
   
   
     return (
       <Container>
         {/* 提交框 */}
         <Paper elevation={3} style={paperStyle}>
           <h1>Add Student</h1>
           <Box
             component="form"
             sx={{
               '& > :not(style)': { m: 1 },
             }}
             noValidate
             autoComplete="off"
           >
             <TextField id="outlined-basic" label="Student Name" variant="outlined" fullWidth
               value={name}
               onChange={(e) => setName(e.target.value)}
             />
   
             <TextField id="outlined-basic" label="Student Address" variant="outlined" fullWidth
               value={address}
               onChange={(e) => setAddress(e.target.value)}
             />
   
             <Button variant="contained" color="secondary" onClick={handleClick}>
               Submit
             </Button>
   
           </Box>
           {name}
           {address}
         </Paper>
   
         {/* 展示框 */}
         <Paper elevation={3} style={paperStyle}>
           <h1>List Students</h1>
           {students.map(student => (
             <Paper elevation={6} style={{ margin: "10px", padding: "15px", textAlign: "left" }} key={student.id}>
               <div>
                 Id: {student.id}<br />
                 Name: {student.name}<br />
                 Address: {student.address}
               </div>
   
               <Button variant="contained" color="primary" onClick={() => handleUpdate(student.id)}>
                 Modify
               </Button>
   
               <Button variant="contained" color="secondary" onClick={() => handleDelete(student.id)}>
                 Delete
               </Button>
             </Paper>
           ))}
         </Paper>
       </Container>
     );
   }
   ```

4. 创建主程序 `App.js`

   ```js
   import './App.css';
   // 引入 Appbar.js 文件
   import Appbar from './components/Appbar';
   // 引入 Student.js 文件
   import Student from './components/Student';
   
   // APP 主函数
   function App() {
     return (
       <div className="App">
         {/* 调用 Appbar.js 中的 Appbar 函数 */}
         <Appbar />
   
         {/* 调用 Student.js 中的 Student 函数 */}
         <Student />
       </div>
     );
   }
   export default App;
   ```

5. 生成静态文件夹

6. 通过 GitLab Pipeline 生成 Image

   - .gitlab-ci.yml

     ```yaml
     variables:
       IMAGE_NAME: jerrybaijy/student-springboot-react-frontend
       IMAGE_TAG: v1.0
     
     stages: 
       - build
     
     build_image:
       stage: build
       image: docker:20.10.20
       services:
         - docker:20.10.20-dind
       variables:
         DOCKER_TLS_CERTDIR: "/certs"
       before_script:
         - docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
       script:
         - docker build -t $IMAGE_NAME:$IMAGE_TAG .
         - docker push $IMAGE_NAME:$IMAGE_TAG
     ```

   - Dockerfile

     ```dockerfile
     FROM node:latest
     WORKDIR /app
     COPY ./build .
     RUN npm install -g http-server
     CMD ["http-server", "-p", "8080"]
     ```

7. 使用 Argo CD 在集群中部署

   - application.yaml

     ```yaml
     apiVersion: argoproj.io/v1alpha1
     kind: Application
     metadata:
       name: student-springboot-react-frontend
       namespace: argocd
     
     spec:
       project: default
       source:
         repoURL: https://gitlab.com/jerrybai/student-springboot-react-frontend.git
         targetRevision: HEAD
         path: dev
       
       destination:
         server: https://kubernetes.default.svc
         namespace: student-springboot-react-frontend
     
       syncPolicy:
         syncOptions:
           - CreateNamespace=true
         automated:
           selfHeal: true
           prune: true
     ```

   - deploymnet.yaml

     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: student-springboot-react-frontend
     spec:
       selector:
         matchLabels:
           app: student-springboot-react-frontend
       replicas: 1
       template:
         metadata:
           labels:
             app: student-springboot-react-frontend
         spec:
           containers:
             - name: student-springboot-react-frontend
               image: jerrybaijy/student-springboot-react-frontend:v1.0
               ports:
                 - containerPort: 8080
               env:
                 - name: PORT
                   value: "8080"
               resources:
                 requests:
                   memory: "1Gi"
                   cpu: "500m"
                   ephemeral-storage: "1Gi"
                 limits:
                   memory: "1Gi"
                   cpu: "500m"
                   ephemeral-storage: "1Gi"
     ```

   - service.yaml

     ```bash
     apiVersion: v1
     kind: Service
     metadata:
       name: student-springboot-react-frontend
     spec:
       selector:
         app: student-springboot-react-frontend
       type: LoadBalancer
       ports:
         - port: 80
           targetPort: 8080
     ```

## 数据库

1. 使用 Argo CD 在集群中部署数据库 MySQL

2. application.yaml

   ```yaml
   apiVersion: argoproj.io/v1alpha1
   kind: Application
   metadata:
     name: student-springboot-react-database
     namespace: argocd
   
   spec:
     project: default
     source:
       repoURL: https://gitlab.com/jerrybai/student-springboot-react-database.git
       targetRevision: HEAD
       path: dev
     
     destination:
       server: https://kubernetes.default.svc
       namespace: student-springboot-react-database
   
     syncPolicy:
       syncOptions:
         - CreateNamespace=true
       automated:
         selfHeal: true
         prune: true
   ```

3. deploymnet.yaml

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: student-springboot-react-database
   spec:
     selector:
       matchLabels:
         app: student-springboot-react-database
     replicas: 1
     template:
       metadata:
         labels:
           app: student-springboot-react-database
       spec:
         containers:
           - name: student-springboot-react-database
             image: jerrybaijy/student-springboot-react-database:v1.0
             ports:
               - containerPort: 3306
             env:
               - name: PORT
                 value: "3306"
             resources:
               requests:
                 memory: "1Gi"
                 cpu: "500m"
                 ephemeral-storage: "1Gi"
               limits:
                 memory: "1Gi"
                 cpu: "500m"
                 ephemeral-storage: "1Gi"
   ```

4. service.yaml

   ```bash
   apiVersion: v1
   kind: Service
   metadata:
     name: student-springboot-react-database
   spec:
     selector:
       app: student-springboot-react-database
     type: ClusterIP
     ports:
       - port: 3306
         targetPort: 3306
   ```
