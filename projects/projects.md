# Student Spring Boot React Full Stack

## 项目概述

- **来源**：[YouTube 博主 Arjun Full Stack web application using Spring Boot and React | REST API | MySQL | React Hooks](https://www.youtube.com/watch?v=O_XL9oQ1_To)
- **项目概述**：这是一个全栈 Web 应用项目，主要功能是网页端与数据库的数据交互。
- **前端**：使用 Java Script 的 React 框架搭建
- **后端**：使用 Java 的 Spring Boot 框架搭建
- **数据库**：使用 XAMPP 集成的 MySQL
- **代码存储**：前后端以两个分项目形式分别存储在托管平台
  - student-springboot-react-frontend
  - student-springboot-react-backend


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
  
  import jakarta.persistence.Entity;
  import jakarta.persistence.GeneratedValue;
  import jakarta.persistence.GenerationType;
  import jakarta.persistence.Id;
  
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

### resources 

- 提前完成数据库搭建

- 连接数据库：resources / application.properties

  ```properties
  # configuration
  spring.jpa.hibernate.ddl-auto=update
  spring.datasource.url=jdbc:mysql://localhost:3306/fullstack
  spring.datasource.username=root
  spring.datasource.password=
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  ```

  删掉了原文件自动生成的一句代码：`spring.application.name=studentsystem`

- 此时转到 StudentsystemApplication.java 文件即可运行应用，验证数据库启动成功

- 在数据库 Admin 页面可以看到已经创建了 student 数据表

### service

- 服务接口：service / StudentService.java

  ```java
  package com.jerrycodes.studentsystem.service;
  
  import com.jerrycodes.studentsystem.model.Student;
  
  public interface StudentSercice {
      public Student saveStudent(Student student);
  }
  ```

- 服务实现：service / StudentServicelmpl.java

  ```java
  package com.jerrycodes.studentsystem.service;
  
  import com.jerrycodes.studentsystem.model.Student;
  import com.jerrycodes.studentsystem.repository.StudentRepository;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Service;
  
  @Service
  public class StudentServicelmpl implements StudentService{
      
      // 连接数据库
      @Autowired
      private StudentRepository studentRepository;
      
      // 保存
      // Ctrl + O - SaveStudent(student:Student):Student
      @Override
      public Student saveStudent(Student student) {
          return studentRepository.save(student);
      }
      // 获取：Alt + Insert - Override Methods... - getALLStudents():List<Student>
  }
  ```

### controller

- 用于映射所有 http 方法：controller / StudentController.java

  ```java
  package com.jerrycodes.studentsystem.controller;
  
  import com.jerrycodes.studentsystem.model.Student;
  import com.jerrycodes.studentsystem.service.StudentService;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.web.bind.annotation.PostMapping;
  import org.springframework.web.bind.annotation.RequestBody;
  import org.springframework.web.bind.annotation.RequestMapping;
  import org.springframework.web.bind.annotation.RestController;
  
  @RestController
  @RequestMapping("/student")
  public class StudentController {
      @Autowired
      private StudentService studentService;
  
      @PostMapping("/add")
      public String add(@RequestBody Student student){
          studentService.saveStudent(student);
          return "New student is added";
      }
  }
  ```


### 启动

- 启动 APP 后端
- 使用 Postman 模拟前端浏览器与后端交互
- 测试通过即可转向前端开发

## 数据库

- **工具**：使用 XAMPP 集成的 Apache MySQL Tomcat 创建数据库
- 启动 XAMPP，创建数据库 fullstack

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

2. 组件 `Appbar.js`

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

3. 组件  `Student.js`

   ```js
   import * as React from 'react';
   import Box from '@mui/material/Box';
   import TextField from '@mui/material/TextField';
   import { Button, Container, Paper } from '@mui/material';
   
   // 此处的 Student 即主程序文件 App.js 中的 <Student />
   export default function Student() {
     const paperStyle = { padding: '50px 20px', width: 600, margin: '20px auto' }
   
     // POST
     const [name, setName] = React.useState('')
     const [address, setAddress] = React.useState('')
   
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
       })
     }
   
     // GE
     const [students, setStudents] = React.useState([])
   
     React.useEffect(() => {
       fetch("http://localhost:8080/student/getAll")
         .then(res => res.json())
         .then((result) => {
           setStudents(result);
         })
     })
   
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
           <h1>Students</h1>
           {students.map(student => (
             <Paper elevation={6} style={{ margin: "10px", padding: "15px", textAlign: "left" }} key={student.id}>
               Id:{student.id}<br/>
               Name:{student.name}<br/>
               Address:{student.address}
   
             </Paper>
           ))}
         </Paper>
       </Container>
     );
   }
   ```

4. 主程序 `App.js`

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

   





