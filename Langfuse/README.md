# Langfuse




## 📦 <b>Requirements</b>
•	Node.js and npm (https://nodejs.org/en )
<br>
•	npm install -g npm@10.2.0

## 📦 <b>Installation</b>
```shell
git clone https://github.com/langfuse/langfuse.git
```
```shell
cd langfuse
```
```shell
docker compose up -d
```
```shell
$env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
```
```shell
$env:DIRECT_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
```
```shell
npx prisma migrate deploy
```
## 📦 <b>Terminal View</b>
![Img](Images/docker.png)
![Img](Images/docker_2.png)
![Img](Images/install.png)
![Img](Images/install_2.png)

## 📦 <b>Create account</b>
![Img](Images/acc.png)
![Img](Images/acc_2.png)

## 📦 <b>Navigate to settings</b>
![Img](Images/settings.png)
![Img](Images/settings_2.png)

## 📦 <b>API Generation</b>
![Img](Images/api.png)

### 📦 <b>Integration</b>
<b>Open the env where you have installed Langflow and pass on the following commands</b>
```shell
set LANGFLOW_LANGFUSE_SECRET_KEY=<your secret key>
```
```shell
set LANGFLOW_LANGFUSE_PUBLIC_KEY=<your public key>
```
```shell
set LANGFLOW_LANGFUSE_HOST=http://localhost:3000
```

### 📦 <b>To verify</b>

```shell
echo $LANGFLOW_LANGFUSE_SECRET_KEY
```
```shell
echo $LANGFLOW_LANGFUSE_PUBLIC_KEY
```
### 📦 <b>Start Langflow</b>
```shell
langflow run
```
<b>Run the flows you desire. After running it you can see the traces on langfuse interface.</b>

### 📦 <b>Output</b>
![Img](Images/dashboard.png)
