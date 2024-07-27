## 项目操作

- 安装
    ```bash
    npm install -g hexo-cli  
  ```

- 初始化
    ```bash
    hexo init  
  ```

- 启动
    ```bash
    hexo server
    ```
- 生成

    ```bash
    hexo generate
    ```
- 部署

    ```bash
    hexo deploy
    ```
  
- 依赖

    ```bash
    npm install
    ```

#### 在 Hexo 中，默认有三种布局：post、page 和 draft。每种布局创建的文件会保存到不同的路径。以下是每种布局的详细说明：

1. Post
- **描述**: 用于创建博客文章。
- **保存路径**: source/_posts 目录。
- **创建命令**:
```bash
hexo new post <post-title>
```
- **示例**:
```bash

hexo new post "My New Post"
```
这将创建一个名为 My New Post.md 的文件，保存到 source/_posts 目录。
2. Page
- **描述**: 用于创建单独的页面，如关于页面、联系页面等。
- **保存路径**: source/<page-name> 目录。
- **创建命令**:
```bash

hexo new page <page-name>
```
- **示例**:
```bash

hexo new page about
```
这将创建一个名为 index.md 的文件，保存到 source/about 目录。
3. Draft

- **描述**: 用于创建草稿，草稿不会被生成和部署。
- **保存路径**: source/_drafts 目录。
- **创建命令**:
```bash
hexo new draft <draft-title>
```
- **示例**:
```bash
hexo new draft "My Draft Post"
```
这将创建一个名为 My Draft Post.md 的文件，保存到 source/_drafts 目录。
4. 发布草稿
如果你有一个草稿准备发布，可以使用以下命令将其移动到 _posts 文件夹中：

```bash
hexo publish <draft-title>
```
### 总结
hexo new post <post-title>：创建博客文章，保存到 source/_posts。
hexo new page <page-name>：创建单独页面，保存到 source/<page-name>。
hexo new draft <draft-title>：创建草稿，保存到 source/_drafts。
hexo publish <draft-title>：发布草稿，将草稿从 source/_drafts 移动到 source/_posts。
