# Kubernetes 基础

## 环境搭建

- Kubernete 需运行在 Docker 基础上
- 在本地使用 Minikube 搭建集群
- 在 Cloud 中搭建集群

## Minikube

​	Minikube 用于创建本地集群，供学习使用，不能用于生产环境。

- **Minikube 安装**

  ```bash
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  ```

- **Minikube 管理**

  ```bash
  # 列出 minkube 配置文件
  minikube profile list
  ```

- **基础命令**

  ```bash
  # 查看集群
  minikube status
  # 创建集群
  minikube start
  # 删除集群
  minikube delete
  ```

## Kubectl

​	kubectl 命令行工具用于与集群交互

- 安装 kubectl

  ```bash
  # 安装 kubectl
  sudo snap install kubectl --classic
  # 添加环境变量
  export PATH=$PATH:/snap/bin
  # 验证安装
  kubectl version --client
  ```

  解释：

  - `--classic` 用于允许 kubectl 访问系统上的文件系统。
  - `--client` 用于告诉 kubectl 仅显示客户端版本信息，而不连接到 Kubernetes 集群来获取服务器版本信息。

## 命令

- **通用命令**

  ```bash
  # 查看 get
  kubectl get pods
  
  # 删除 delete
  kubectl delete pods
  
  # 应用 apply
  kubectl apply -f $YAML # `-f` 指定路径
  
  # 查看pod
  kubectl logs $POD_NAME -n $NAME_SPACE # -n指定命名空间
  ```

- **常用命令**

  ```bash
  
  ```

## 命令选项

-  **-n $NAMESPACE**：指定命名空间
- 

## K8S 架构

![Kubernetes架构图](assets/Kubernetes架构图.png)

# Cluster

## Cluster 基础

- **基础命令**

  ```bash
  # 查看 Cluster
  kubectl cluster-info
  # 停止 Cluster
  systemctl stop kubelet
  ```

# Namespace

## Namespace 基础

​	Namespace（命名空间）是 Kubernetes 中用于隔离和组织资源的虚拟工作空间。它是一种在逻辑上划分集群资源的方式，允许在同一集群内创建多个虚拟的独立环境。

- **基础命令**

  ```bash
  # 创建 namespace
  kubectl create namespace NAMESPACE_NAME
  # 删除 namespace
  kubectl delete namespace NAMESPACE_NAME
  ```

# Deployment

## Deployment 基础

​	Deployment（部署）是 Kubernetes 中用于管理 Pod 和 ReplicaSet 的控制器。它定义了您希望部署的应用程序的期望状态，并负责确保集群中的实际状态与所定义的状态匹配。

- **基础命令**

  ```bash
  # 查看deployment
  kubectl get deployment
  # 手动创建 deployment
  kubectl create deployment DEPLOYMENT_NAME --image=IMAGE
  # YAML 文件创建 deployment
  kubectl apply -f deployment.yaml
  # 删除 deployment
  kubectl delete deployment DEPLOYMENT_NAME
  ```

- **deployment.yaml**

  ```yaml
  apiVersion: apps/v1              # API 版本
  kind: Deployment                 # 资源类型
  metadata:                        # 资源元数据
    labels:                        # 资源标签
      $KEY: $VLUE                  # 资源的标签键值对，可以用来标识和分类资源
    name:                          # Deploymnet 名称
    namespace:                     # Deploymnet 命名空间
  spec:                            # Deploymnet 规格
    replicas:                      # Pod 数量
    selector:                      # 标签选择器，用于选择要管理的 Pod
      matchLabels:                 # 匹配标签
        $KEY: $VLUE                # 标签选择器中用于匹配的标签键值对
    template:                      # Pod 模板
      metadata:                    # Pod 元数据
        labels:                    # Pod 标签
          $KEY: $VLUE              # Pod 的标签键值对
      spec:                        # Container 规格
        containers:                # Container 列表
        - image:                   # Image 地址
          imagePullSecrets:        # Image 下载策略
          name:                    # Container 名称
          args:                    # ENTRYPOINT 参数
          commnd:                  # 执行命令
          ports:                   # Container 公开端口
          env:                     # 环境变量
          resources:               # 容器资源限制和请求
            requests:                               # 请求资源
              memory: "1Gi"                         # 请求内存为 1Gi
              cpu: "500m"                           # 请求 CPU 为 500m
              ephemeral-storage: "1Gi"              # 请求临时存储为 1Gi
            limits:                                 # 资源限制
              memory: "1Gi"                         # 内存限制为 1Gi
              cpu: "500m"                           # CPU 限制为 500m
              ephemeral-storage: "1Gi"              # 临时存储限制为 1Gi
          livenessProbe:           # 存活检查
          readinessProbe:          # 就绪检查
          startupProbe:            # 启动检查
          volumeMounts:            # 卷挂载
          securityContext:         # 安全上下文
          lifecycle:               # 容器生命周期回调
        volumes:                   # Pod 的卷列表
  ```

  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      app: jerry-app
    name:
    namespace:
  spec:
    replicas:
    selector:
      matchLabels:
        app: jerry-app
    template:
      metadata:
        labels:
          app: jerry-app
      spec:
        containers:
        - image:
          imagePullSecrets:
          name:
          args:
          commnd:
          ports:
          env:
          resources:
            requests:
              memory: "1Gi"
              cpu: "500m"
              ephemeral-storage: "1Gi"
            limits:
              memory: "1Gi"
              cpu: "500m"
              ephemeral-storage: "1Gi"
          livenessProbe:
          readinessProbe:
          volumeMounts:
          securityContext:
          lifecycle:
        volumes:
  ```

# Node

# Pod

# Service

- **基础命令**

  ```bash
  # 查看 service
  kubectl get svc [-n NAMESPACE]
  ```

- **service.yaml**

  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: $SERVICE_NAME
  spec:
    selector:
      $KEY: $VALUE
    type: LoadBalancer
    ports:
      - port: 80
        targetPort: 8080
  ```
  
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: myapp-service
  spec:
    selector:
      app: myapp
    type: LoadBalancer            # 如本地访问服务类型为 ClusterIP
    ports:                        # 服务监听的端口列表
      - port: 80                  # 公网端口 80
        targetPort: 8080          # Pod 端口 8080
  ```
  
- **port**

  - **公开至公网**

    方法一：将现有服务的类型更改为 LoadBalancer 类型
  
    ```bash
    kubectl patch svc $SERVICE_NAME -n $NAMESPACE -p '{"spec": {"type": "LoadBalancer"}}'
    ```
  
    方法二：为 Deployment 创建一个新的 Service，并将其类型设置为 LoadBalancer
  
    ```bash
    kubectl expose deployment $DEPLOYMENT_NAME --type LoadBalancer --port 80 --target-port 8080
    ```
  
  - **公开至本地**
  
    ```bash
    kubectl port-forward deployment/$DEPLOYMENT_NAME $HOST_PORT:$POD_PORT
    # eg
    kubectl port-forward deployment/nginx 80:8080
    ```
    
    

# Argo CD

## Argo CD 基础

​	Argo CD 是一个持续部署工具，可以通过修改 yaml 文件，改变应用的运行。

​	![argo-cd](assets/argo-cd.png)

### 环境搭建

1. Linux 系统，Docker 已安装，kubectl 已安装，启动一个集群。

2. 安装 Argo CD

   ```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```

3. 查看 pod 状态，直到全部运行

   ```bash
   kubectl get pod -n argocd
   ```

4. 将端口转发至本地或公网即可查看 Argo CD UI 界面

   ```bash
   kubectl get svc -n argocd
   # 本地
   kubectl port-forward -n argocd svc/argocd-server 8080:443
   # 公网
   kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
   ```
   
5. 获取密码

   ```bash
   # 获取密码
   kubectl get secret argocd-initial-admin-secret -n argocd -o yaml
   # 解码，PASSWORD为上一步获取到的加密密码
   echo $PASSWORD== | base64 --decode
   
   # 上次密码OaVoMpufPwfd-X-9
   ```

6. 在本地或公网通过 IP 访问 Argo CD 页面登录，用户名为admin，公网访问需要科学上网

## 基本流程

1. Argo CD 已安装

2. UI 界面创建 Git 仓库，clone 至本地

3. Repo 根目录创建 dev 目录

4. dev 目录创建 deployment.yaml 和 service.yaml

   1. 注意云上的集群有节点限制，试用时只能创建一个副本
   2. deployment.yaml 和 service.yaml 见 Kubenetes

5. Repo 根目录创建 application.yaml

   ```yaml
   apiVersion: argoproj.io/v1alpha1
   kind: Application
   metadata:
     name: student-springboot-react-frontend
     namespace: argocd
   
   spec:
     project: default
     source:
       repoURL: https://github.com/Jerrybaijy/student-springboot-react-frontend.git
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

6. 推送仓库

7. 部署应用

   ```bash
   kubectl apply -f application.yaml
   ```

8. 在 Argo CD 页面查看应用已启动

9. 查看 IP 即可访问应用（如有需要可进行端口转发）

   ```bash
   kubectl get svc -n myapp
   ```

10. 以后若想更改应用，只需需改 yaml 文件并推送至 Git 仓库，Argo CD 可自动识别自动部署。

11. 删除应用

    1. 不要直接在集群删除应用，要先在 Argo CD 页面删除应用（因为已配置自愈，Argo CD 会自动创建应用）
    2. 再删除应用的命名空间

12. 删除 Argo CD

    1. **删除 ArgoCD 自定义资源定义（CRD）**

       ```bash
       kubectl delete crd applications.argoproj.io appprojects.argoproj.io argocds.argoproj.io
       ```

    2. **删除 ArgoCD 的命名空间**

       ```bash
       kubectl delete namespace 
       ```

## 相关项目

- Argo CD Git
- Argo CD Helm

## 解决方案

### OutOfSync

1. 当使用 ArgoCD 部署好应用以后，一切运行正常，但 UI 页面一直显示 OutOfSync，即使状态不同步，应用程序实际上也是同步的，但看到它不同步很烦人。若要消除此问题，有一种解决方案是使用资源排除。

   ![image-20240329143514361](assets/image-20240329143514361.png)

2. 访问 Argo CD 的 configmap

   ```bash
   KUBE_EDITOR="nano" kubectl edit cm argocd-cm -n argocd
   ```

   ![image-20240329143851461](assets/image-20240329143851461.png)

3. 使用 nano 编辑器编辑此配置图

   ```bash
   KUBE_EDITOR="nano" kubectl edit cm argocd-cm -n argocd
   ```

4. 文末在第一层级添加以下数据并保存

   ```yaml
   data:
     resource.exclusions: |
       - apiGroups:
         - cilium.io
         kinds:
         - CiliumIdentity
         clusters:
         - "*"
   ```

# Helm

Helm 是 Kubernetes 的包管理器，使用 "chart" 的打包格式来描述 Kubernetes 资源的集合，使得部署和管理应用程序变得更加简单和可重复。

## 环境搭建

- 集群已运行，Kubectl 已安装

- Linux 安装（Debian / Ubuntu）

  ```bash
  sudo snap install helm --classic
  # 添加环境变量
  export PATH="$PATH:/snap/bin"
  ```

- Windows 安装

  ```bash
  # 提前安装包管理器 Chocolatey，详见 Windows
  choco install kubernetes-helm
  ```

## Helm 基础

- **命令**

  ```bash
  # 查看 helm 版本
  helm version
  
  # 查看 chart 配置值（values.yaml 文件中的值）
  helm show values .
  
  # 重置 index
  helm repo index $CHART_PATH --url https://jerrybaijy.github.io/$REPO/
  ```

## 基本流程

### 建立远程仓库

1. UI 界面创建 Git 仓库，clone 至本地

2. Repo 根目录创建创建 Chart

   ```bash
   helm create $CHART_NAME
   ```

3. 配置 Chart
   1. 编辑模板 `mychart/templates`
   2. 编辑 values `mychart/values.yaml`

4. 封装 Chart

   ```bash
   helm package $CHART_PATH
   ```

5. 重置 index

   ```bash
   helm repo index $CHART_PATH
   ```

6. Git 推送，GitHub 设置 Pages - Branch（一定不要提前设置）

7. 重置 index

   ```bash
   helm repo index $CHART_PATH --url https://jerrybaijy.github.io/$REPO/
   ```

8. Git 推送

9. 至此，远程 Helm Chart 仓库已建好，可供其它调用：https://jerrybaijy.github.io/$REPO/

### 使用远程仓库

1. 添加本地 Helm 仓库，与远程仓库关联

   ```bash
   helm repo add $HELM_REPO https://jerrybaijy.github.io/$REPO
   ```

2. 使用 Helm Charts

   ```bash
   helm install $RELEASE $HELM_REPO/$CHART_NAME
   ```

### 流程实例

- 这是项目 Argo CD Git 的步骤留存，最后两大步取一个操作

  ```bash
  # UI 界面创建 Git 仓库，clone 至本地，进入 repo 目录
  
  helm create argocd-helm-chart
  helm package argocd-helm-chart
  helm repo index .
  
  # Git 推送，GitHub 设置 Pages - Branch（一定不要提前设置）
  
  helm repo index . --url https://jerrybaijy.github.io/argocd-helm/
  
  # Git 推送
  
  # 1.以下是本地使用远程 Helm Charts
  helm repo add argocd-helm https://jerrybaijy.github.io/argocd-helm/
  kubectl create namespace argocd-helm
  helm install argocd-helm-app argocd-helm/argocd-helm-chart -n argocd-helm
  kubectl get pod -n argocd-helm
  kubectl get svc -n argocd-helm
  kubectl delete namespace argocd-helm
  
  # 2.以下是 Argo CD 使用远程 Helm Charts
  kubectl apply -f application.yaml
  kubectl get namespace
  kubectl get pod -n argocd-helm
  kubectl get svc -n argocd-helm
  kubectl delete namespace argocd-helm
  ```

## Helm Repo

- **基础命令**

  ```bash
  # 查看 Helm Repo
  helm repo list
  # 添加 Helm Repo
  helm repo add $HELM_REPO https://jerrybaijy.github.io/$REPO
  # 删除 Helm Repo
  helm repo remove $HELM_REPO
  # 删除所有 Helm Repo
  rm ~/.config/helm/repositories.yaml
  ```

- Helm Repo 实际只是一个 YAML 文件，存储于 `~/.config/helm/repositories.yaml`，里面声明了各个 Helm Repo 与 Remote Repo 的对应关系。

## Chart

- **基础命令**

  ```bash
  # 查看 chart 信息
  helm show chart .
  # 创建 chart
  helm create $CHART_NAME
  # 封装 chart
  helm package $CHART_PATH
  # 发布 chart，没用过
  helm push $CHART $CHART_REPO
  # 测试 chart
  helm lint $CHART
  ```

## Release

- **基础命令**

  ```bash
  # 查看 release
  helm list
  # 部署 release
  helm install $RELEASE $HELM_REPO/$CHART_NAME
  # 删除 release
  # 测试 release
  helm test $RELEASE
  ```

## Values

- values.yaml

  ```yaml
  # 副本数量
  replicaCount: 2
  
  image:
    repository: jerrybaijy/jerry-image
    tag: "v1.0"
    pullPolicy: IfNotPresent
  
  imagePullSecrets: []
  nameOverride: ""
  fullnameOverride: ""
  
  serviceAccount:
    # Specifies whether a service account should be created
    create: true
    # Automatically mount a ServiceAccount's API credentials?
    automount: true
    # Annotations to add to the service account
    annotations: {}
    # The name of the service account to use.
    # If not set and create is true, a name is generated using the fullname template
    name: ""
  
  podAnnotations: {}
  podLabels: {}
  
  podSecurityContext: {}
    # fsGroup: 2000
  
  securityContext: {}
    # capabilities:
    #   drop:
    #   - ALL
    # readOnlyRootFilesystem: true
    # runAsNonRoot: true
    # runAsUser: 1000
  
  service:
    type: ClusterIP
    port: 80
  
  ingress:
    enabled: false
    className: ""
    annotations: {}
      # kubernetes.io/ingress.class: nginx
      # kubernetes.io/tls-acme: "true"
    hosts:
      - host: chart-example.local
        paths:
          - path: /
            pathType: ImplementationSpecific
    tls: []
    #  - secretName: chart-example-tls
    #    hosts:
    #      - chart-example.local
  
  resources: {}
    # We usually recommend not to specify default resources and to leave this as a conscious
    # choice for the user. This also increases chances charts run on environments with little
    # resources, such as Minikube. If you do want to specify resources, uncomment the following
    # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
    # limits:
    #   cpu: 100m
    #   memory: 128Mi
    # requests:
    #   cpu: 100m
    #   memory: 128Mi
  
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
    # targetMemoryUtilizationPercentage: 80
  
  # Additional volumes on the output Deployment definition.
  volumes: []
  # - name: foo
  #   secret:
  #     secretName: mysecret
  #     optional: false
  
  # Additional volumeMounts on the output Deployment definition.
  volumeMounts: []
  # - name: foo
  #   mountPath: "/etc/foo"
  #   readOnly: true
  
  nodeSelector: {}
  
  tolerations: []
  
  affinity: {}
  ```

