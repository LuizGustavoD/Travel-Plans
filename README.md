# ✈️ Travel Planner AI

Um projeto web interativo que utiliza inteligência artificial para gerar planos de viagem personalizados com base em dois destinos informados pelo usuário. Desenvolvido com **React + TailwindCSS** no frontend, **Flask** no backend e consumo da **API da OpenAI** para elaboração dos roteiros.

---

## 🧠 Funcionalidades

- 🗺️ Geração de um plano de viagem personalizado com base em **dois destinos**.
- 🤖 Utilização da **API da OpenAI** para criação de roteiros inteligentes e detalhados.
- 🌐 Interface moderna, responsiva e intuitiva com **React e TailwindCSS**.
- ⚙️ Backend leve com **Flask**, responsável por processar os inputs e integrar com a API.

---

## 📸 Demonstração

![Demonstração](exemplo.gif) <!-- Substitua por uma imagem ou GIF do funcionamento do app -->

---

## 🚀 Tecnologias Utilizadas

### Frontend
- [React](https://reactjs.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [Vite](https://vitejs.dev/) *(caso esteja usando)*

### Backend
- [Flask](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
- [OpenAI API](https://platform.openai.com/docs)

---

## 🛠️ Como Rodar o Projeto

### Pré-requisitos
- Node.js e npm
- Python 3.10+
- Chave da OpenAI API

### Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
export OPENAI_API_KEY="sua-chave-aqui"  # ou usar um .env
python app.py
Frontend (React)
bash
Copiar
Editar
cd frontend
npm install
npm run dev
🔐 Variáveis de Ambiente
No backend, é necessário configurar a variável de ambiente:

bash
Copiar
Editar
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Você pode colocar isso em um arquivo .env e carregar com python-dotenv, se desejar.

📁 Estrutura do Projeto
arduino
Copiar
Editar
travel-planner/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── tailwind.config.js
│   └── ...
│
└── README.md
💡 Melhorias Futuras
📍 Sugestão automática de atrações turísticas.

🗓️ Geração de itinerário dia a dia.

💬 Tradução dos roteiros para outros idiomas.

📦 Deploy com integração CI/CD.

📱 Versão mobile com PWA.

👨‍💻 Autor
Desenvolvido por Luiz Gustavo Damas
LinkedIn · GitHub