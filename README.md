# 💈 Sistema de Agendamento para Barbearia

> ⚠️ **Atenção:** Este projeto está em desenvolvimento e algumas funcionalidades ainda podem ser adicionadas ou aprimoradas.

Este projeto é um sistema web desenvolvido em Django para gerenciar agendamentos em uma barbearia. Permite cadastrar clientes, serviços oferecidos e controlar os horários disponíveis para agendamento.

---

## 🚀 Funcionalidades

- 🧑‍🤝‍🧑 Cadastro de clientes.  
- ✂️ Cadastro de serviços com duração e preço.  
- 📅 Agendamento de horários disponíveis (validação para horários cheios).  
- 📋 Listagem de agendamentos para o dono da barbearia (com login).  
- 🔐 Login e logout do administrador/dono da barbearia.  

---

## 🛠 Tecnologias utilizadas

- 🐍 Python
- 🌐 Django  
- 💾 SQLite (padrão Django) ou outro banco configurado  
- 🎨 HTML, CSS para templates  

---

## 🗂 Estrutura do projeto

- **models.py:** Define os modelos Cliente, Serviço e Agendamento.  
- **views.py:** Controla a lógica de agendamento, listagem e autenticação.  
- **templates:** Arquivos HTML com CSS para o front-end. 
- **urls.py:** Rotas do sistema.  

---

## 🎯 Como usar

1. 📥 Clone o repositório.  
2. 🐍 Crie e ative um ambiente virtual Python:  
   - No Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```  
   - No Linux/Mac:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```  
3. 📦 Instale as dependências (`pip install -r requirements.txt`).  
4. 🛠 Execute as migrações (`python manage.py migrate`).  
5. 👤 Crie um superusuário (`python manage.py createsuperuser`).  
6. 🚀 Rode o servidor (`python manage.py runserver`).  
7. 🌐 Acesse no navegador `http://localhost:8000` para usar o sistema.  

---

## ✨ Ideias futuras

- 🎨 Interface mais amigável e responsiva.  
- 🔔 Sistema de notificações para agendamentos.  
- 📊 Relatórios e histórico de clientes.  
- 📱 Integração com APIs externas para SMS/email.  

---

## 📞 Contato

Qualquer dúvida ou sugestão, entre em contato: brunocamargo.dev@gmail.com
