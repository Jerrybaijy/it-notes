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
    name: myapp-service
  spec:
    selector:
      app: myapp
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
    type: LoadBalancer            # 服务类型为 LoadBalancer，用于将外部流量引导到 Pod，如本地访问服务类型为 ClusterIP
    ports:                        # 服务监听的端口列表
      - port: 80                  # 公网端口 80
        targetPort: 8080          # Pod 端口 8080
  ```
  
- **port**

  - 在 Kubernetes 集群中创建一个 Service 资源，将其暴露为外部的负载均衡服务

    ```bash
    # `--port` 公网端口 80，`--target-port` 应用端口 8080
    kubectl expose deployment $DEPLOYMENT_NAME --type LoadBalancer --port 80 --target-port 8080
    ```

    ```bash
    kubectl patch svc $SERVICE_NAME -n $NAMESPACE -p '{"spec": {"type": "LoadBalancer"}}'
    ```
  
  - 在本地计算机和 Kubernetes 集群中的 Pod 之间建立端口转发
  
    ```bash
    kubectl port-forward deployment/$DEPLOYMENT_NAME $HOST_PORT:$POD_PORT
    # eg
    kubectl port-forward deployment/nginx 80:8080
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

- **常用命令**

  ```bash
  # 查看 helm 版本
  helm version
  # 创建 chart
  helm create $CHART_NAME
  # 查看 chart 信息
  helm show chart .
  # 查看 chart 配置值（values.yaml 文件中的值）
  helm show values .
  # 封装 chart（处在包含$CHART_NAME的目录）
  helm package $CHART_NAME
  # 发布 chart
  helm push $CHART_NAME-0.1.0.tgz $REPO_NAME
  # 部署 chart
  helm install $RELEASE_NAME $REPO/$CHART_NAME
  # 删除 release
  
  # 查看 release
  helm list
  # 测试 release
  helm test $RELEASE
  # 测试 chart
  helm lint $CHART
  ```

- **流程**

  ```bash
  创建 Chart
  定义 Kubernetes 资源模板 `mychart/templates`
  定义 Chart 配置值 `mychart/values.yaml`
  封装 Chart
  发布 Chart
  部署 chart
  管理 Chart
  ```

- 步骤

  ```bash
  # ~目录
  helm create $CHART
  helm create front-chart
  
  helm package $CHART
  helm package front-chart
  
  # UI 创建 repo，并 clone 至本地
  
  cd $REPO
  mv ~/test-app-0.1.0.tgz .
  
  cd ..
  # 在 $REPO_PATH 文件夹中生成 index.yaml，此文件中含有 url 信息
  # helm repo index $REPO_PATH --url https://jerrybaijy.github.io/$REPO/
  helm repo index repo5 --url https://jerrybaijy.github.io/repo5/
  
  cd $REPO
  # Git 推送，然后设置 pages branch
  
  kubectl create namespace new
  
  # 将远程的 $REPO 添加至本地的 $HELM_REPO 配置
  helm repo add $HELM_REPO https://jerrybaijy.github.io/$REPO
  helm repo add repo5 https://jerrybaijy.github.io/repo5
  
  helm install $RELEASE_NAME $HELM_REP/$CHART -n $NAMESPACE
  helm install repo5-app repo5/front-chart -n new
  
  kubectl get pod -n new
  kubectl get svc -n new
  kubectl delete namespace new
  ```

- Helm 仓库

  ```bash
  # 查看仓库
  helm repo list
  # 删除仓库
  helm repo remove $REPO_NAME
  # 删除所有仓库
  rm ~/.config/helm/repositories.yaml
  ```

  

## 步骤

1. 创建 chart
2. 封装 chart
3. UI 创建 repo，并 clone 至本地
4. 将 chart 封装文件移动到本地 repo
5. 


## values

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

