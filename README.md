# My Wallet App

## Descripción

**My Wallet App** es una aplicación web diseñada para gestionar cuentas bancarias y realizar transacciones de forma segura. Desarrollada en Python utilizando Flask para el backend y Vue.js para el frontend, esta aplicación ofrece un control de acceso robusto, transferencias entre cuentas, y funciones adicionales como la actualización de datos y congelación de cuentas.

## Características

- **Control de Acceso**: Cada usuario tiene su propio dashboard con sus datos personales, saldo, balance y retenciones.
- **Base de Datos Encriptada**: Utiliza una base de datos encriptada para almacenar información sensible.
- **Transferencias**: Permite transferencias a otras cuentas internas y de terceros.
- **Creación de Usuarios**: Los usuarios pueden crearse solo si tienen una cuenta bancaria válida. Se verifica el nombre, DNI y número de cuenta antes de permitir la creación de usuario.
- **Identificadores Únicos**: Utiliza el DNI y el número de cuenta como identificadores únicos.
- **Funciones Adicionales**: Verificación de saldo, congelación de cuentas y actualización de datos como el correo electrónico.

## Estructura del Proyecto

my_wallet_app/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── forms.py
│ │ ├── utils.py
│ │ ├── routes/
│ │ │ ├── init.py
│ │ │ ├── auth.py
│ │ │ ├── user.py
│ │ │ ├── transaction.py
│ ├── migrations/
│ │ ├── ...
│ ├── tests/
│ │ ├── test_auth.py
│ │ ├── test_user.py
│ │ ├── test_transaction.py
│ ├── .env
│ ├── config.py
│ ├── run.py
│ ├── requirements.txt
│ ├── encrypted_wallet.db
├── frontend/
│ ├── public/
│ │ ├── index.html
│ ├── src/
│ │ ├── components/
│ │ │ ├── Dashboard.vue
│ │ │ ├── Login.vue
│ │ │ ├── CreateUser.vue
│ │ │ ├── UpdateDetails.vue
│ │ │ ├── FreezeAccount.vue
│ │ ├── assets/
│ │ │ ├── css/
│ │ │ │ ├── styles.css
│ │ │ ├── js/
│ │ │ │ ├── scripts.js
│ │ ├── App.vue
│ │ ├── main.js
│ ├── package.json
├── README.md


## Instalación

### Requisitos Previos

- Python 3.6+
- Node.js y npm

### Instalación en Linux

1. **Instalar Dependencias**:
    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip nodejs npm
    ```

2. **Clonar el Repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/my_wallet_app.git
    cd my_wallet_app
    ```

3. **Configurar el Backend**:
    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. **Configurar el Frontend**:
    ```bash
    cd ../frontend
    npm install
    npm run serve
    ```

5. **Iniciar la Aplicación**:
    - Backend:
      ```bash
      cd backend
      source venv/bin/activate
      flask run
      ```
    - Frontend:
      ```bash
      cd frontend
      npm run serve
      ```

### Instalación en Windows

1. **Instalar Dependencias**:
    - Descargar e instalar [Python](https://www.python.org/downloads/)
    - Descargar e instalar [Node.js](https://nodejs.org/)

2. **Clonar el Repositorio**:
    ```cmd
    git clone https://github.com/tu-usuario/my_wallet_app.git
    cd my_wallet_app
    ```

3. **Configurar el Backend**:
    ```cmd
    cd backend
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

4. **Configurar el Frontend**:
    ```cmd
    cd ../frontend
    npm install
    npm run serve
    ```

5. **Iniciar la Aplicación**:
    - Backend:
      ```cmd
      cd backend
      venv\Scripts\activate
      flask run
      ```
    - Frontend:
      ```cmd
      cd frontend
      npm run serve
      ```

## Configuración de Git

### En Linux

1. **Instalar Git**:
    ```bash
    sudo apt update
    sudo apt install git
    ```

2. **Configurar el Nombre de Usuario y Correo Electrónico**:
    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_email@ejemplo.com"
    ```

3. **Verificar la Configuración**:
    ```bash
    git config --list
    ```

### En Windows

1. **Instalar Git**:
    - Descargar e instalar [Git](https://git-scm.com/).

2. **Configurar el Nombre de Usuario y Correo Electrónico**:
    ```cmd
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_email@ejemplo.com"
    ```

3. **Verificar la Configuración**:
    ```cmd
    git config --list
    ```

## Comandos Básicos de Git

- **Clonar un Repositorio**:
    ```bash
    git clone https://github.com/usuario/repo.git
    ```

- **Agregar Archivos al Índice**:
    ```bash
    git add .
    ```

- **Confirmar los Cambios**:
    ```bash
    git commit -m "Mensaje del commit"
    ```

- **Subir Cambios al Remoto**:
    ```bash
    git push origin master
    ```

- **Solicitar y Cargar Cambios del Remoto**:
    ```bash
    git pull origin master
    ```

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los pasos a continuación:

1. **Fork el Repositorio**
2. **Crea una Rama de Feature** (`git checkout -b feature/nueva-feature`)
3. **Commit tus Cambios** (`git commit -m 'Añadir nueva feature'`)
4. **Push a la Rama** (`git push origin feature/nueva-feature`)
5. **Abre un Pull Request**

## Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.
