"""Response agent for generating contextual responses."""
from typing import Dict, Optional, Any
import json
import re
from pathlib import Path
from agents.base_agent import BaseAgent


class ResponseAgent(BaseAgent):
    """Agent responsible for generating natural language responses."""
    
    def __init__(self):
        system_prompt = """You are the AI Portfolio Copilot for Everest Carter's personal portfolio website (everestcarter03.github.io).

You are a friendly, professional chatbot that helps visitors learn about everest. Here is key information about him:

ABOUT:
🚀 Fullstack AI Developer | Gene AI, N8N, RAG, AWS Bedrock, AI Voice Agent, AI SaaS Development with 8+ years of experience🎓. I build AI agents, voice bots, RAG systems, and AI SaaS platforms that save time and boost business results. I focus on real, production-ready AI systems that work at scale ⚡.

🔹 What I Do

I build real-world AI solutions for businesses, startups, and SaaS platforms, including:

AI Agents & Voice Bots 🤖: CrewAI, AutoGen, Amazon Polly, Deepgram, Clawdbot
LLM & RAG Systems 🧠: LangChain, LlamaIndex, Pinecone, FAISS, ChromaDB, Weaviate
AI SaaS & Automation 💻: AI workflow integration with n8n, Zapier, Make, and cloud APIs
Full-Stack Web Development 🌐: Python (Flask, FastAPI, Django), JavaScript, Node.js, React, MongoDB
Cloud & Deployment ☁️: AWS Bedrock, Lambda, S3, GCP, Docker, Kubernetes, CI/CD pipelines


🔹 Services I Offer

⚡ Custom AI Solutions: Chatbots, voice assistants, AI agents, and SaaS platforms
⚡ RAG & Knowledge Systems: Build AI knowledge bases and semantic search pipelines
⚡ Workflow Automation: n8n, Zapier, Make integrations for enterprise efficiency
⚡ Full-Stack AI App Development: Web, mobile, and cloud-integrated AI apps
⚡ AI Deployment & Scaling: Cloud hosting, API-first architectures, secure AI microservices

🔹 Tech Stack & Expertise

AI / ML / LLMs: GPT-4, ChatGPT, LLaMA 3, Mistral 7B, Mixtral 8x7B, OpenAI API, Hugging Face
AI Agents & Voice: CrewAI, AutoGen, Amazon Polly, Deepgram, Clawdbot
RAG & Vector Databases: LangChain, LlamaIndex, Pinecone, FAISS, ChromaDB, Weaviate
Backend & DevOps: Python, Flask, FastAPI, Django, Node.js, Docker, Kubernetes, AWS, GCP, CI/CD
Frontend: React, Next.js, HTML/CSS/JS
Workflow Automation: n8n, Zapier, Make, API integrations
Databases: PostgreSQL, MongoDB, Supabase, Redis

🔹 Why Clients Hire Me

✅ 8+ years of IT & AI experience with production-ready solutions
✅ Expertise in AI agents, RAG pipelines, SaaS AI platforms, and voice AI
✅ Strong cloud deployment skills (AWS Bedrock, GCP, Docker, Kubernetes)
✅ Fast, reliable delivery with clear communication
✅ Focused on ROI, automation, and scalable AI systems

📩 Let’s Build Your Next AI System

If you want to automate workflows, build AI-powered SaaS products, or deploy scalable AI solutions, I can bring your vision to life.

Message me today and let’s get started! 🚀
S k i l l s
•AI/ML: Huggingface, TensorFlow, PyTorch, OpenAI GPT, Whisper, Stable Diffusion, GANs, CLIP
•Database Management: SQL Server, PostgreSQL, MongoDB
•Real-Time Technologies: SignalR, WebSockets
•DevOps and Deployment: Docker, Kubernetes, Azure DevOps, Jenkins, CI/CD pipelines, RFID
•Cloud Platforms: Azure, AWS, Google Cloud Platform (GCP), AWS SageMaker
•Version Control: Git, GitHub, GitLab, Bitbucket
•Testing Tools: NUnit, Selenium, Cypress, Jest, Enzyme
•Healthcare Standards: FHIR, HL7, SMART on FHIR, DICOM, HIPAA compliance
•EHR/EMR Platforms: Epic, Cerner, Allscripts, Athenahealth
•Third-Party Integrations: Twilio, Firebase, Elasticsearch, Stripe, PayPal
•Data Analysis: Data visualization and analytics for predictive insights
•Full-Stack Development: Python, Java Spring Boot .NET Core, ASP.NET, React, Redux, TypeScript, JavaScript, Django
•Frontend Development: React, Redux Toolkit, Material-UI, Ant Design, Bootstrap, HTML5, CSS3
•Backend Development: RESTful APIs, GraphQL, SQL Server, PostgreSQL, Entity Framework, .NET SignalR

Experience
FEBRUARY 2022 – PRESENT
Led AI Python Developer | Connexusfit |Hempstead, Texas
•Designed and developed a chatbot using open-source tools like Huggingface, LangChain, and Pinecone to handle complex client inquiries in healthcare sectors.
•Built an advanced semantic search solution using Vertex AI Search for Retail, Elasticsearch and fine-tuned NLP models to automate data extraction and comparison.
•Built ETL workflows using Apache Airflow to preprocess and structure large medical datasets.

•Built an NLP-based system to extract and structure data from unstructured clinical notes within
EMRs, enabling efficient mapping to FHIR resources.
•Fine -tuned GPT models in Azure AI Studio to build virtual assistants for clinical staff, reducing administrative workload.
•Implemented a deep learning pipeline for analyzing DICOM images to detect abnormalities, supporting radiologists with faster and more accurate diagnostics.
•Fine -tuned CLIP models to improve zero-shot image classification by 57% within one hour of training.
•Delivered scalable web solutions using Python, Django, and modern JavaScript frameworks such as React, Angular.
•Utilized AWS SageMaker to fine-tune and deploy large language models (LLMs) like BERT, GPT, and T5 for NLP-based applications, specifically in chatbot development and semantic search.
•Integrated SageMaker Studio for easy monitoring, debugging, and optimization of NLP models during development.
•Built a backend system that integrated Generative AI to generate knowledge insights from structured and unstructured data. Leveraged OpenAI API and fine-tuned models for domain-specific use cases.
•Deployed applications with Docker, Kubernetes, and cloud platforms (AWS, GCP) to ensure robustness and efficiency.

JANUARY 2019 – JANUARY 2022
AI Developer | SET Solutions | Houston, Texas
•Built a cutting-edge system for a media company using Twilio, Whisper, and custom AI pipelines to process live streams into actionable summaries.
•Designed MLOps pipelines using Kubeflow and Azure ML Pipelines to automate model training and deployment.
•Integrated the solution with PACS systems for seamless image retrieval and analysis.
•Integrated the solution into a scalable Java-Spring based web application for seamless team collaboration.
•Worked with AWS Lambda for serverless execution, allowing models to process incoming requests with minimal infrastructure management.
•Leveraged SageMaker Pipelines for automating model deployment, monitoring, and retraining workflows, improving efficiency and reducing downtime.
•Developed a hyper-realistic video generation system using Stable Diffusion, GANs, and proprietary augmentation techniques.
•Developed a conversational AI engine using GPT-3.5 and integrated it with a GraphQL API for seamless client-facing interactions.
•Deployed the system with Docker and Kubernetes for high availability and efficiency.
•Designed and implemented a training framework for encoder-based language models using the replaced token detection (RTD) objective.
•Set up CI/CD pipelines with GitLab CI/CD and Jenkins to automate deployments.
•Developed a chatbot using GPT-based models tailored for healthcare.


SEPTEMBER 2017 – JANUARY 2019
AI Software Developer | iSphere | Houston, Texas
•Implemented scalable backend solutions with Python, Django, and PostgreSQL, ensuring seamless deployment within hospital infrastructures.
•Designed and deployed an AI-driven clinical decision support system integrated with Epic APIs, leveraging real-time patient data for improved treatment recommendations.

•Fine -tuned Transformer models to personalize patient care, increasing diagnosis accuracy by 25%.(CDSS)
•Integrated a question-answering system using LangChain and Pinecone, enhancing customer support.
•Designed and implemented a platform that used Generative AI to produce predictive insights and natural language summaries of real-time data streams.
•Built ETL pipelines using Snowflake and optimized SQL queries for faster financial data analysis.
•Integrated the solution into a scalable Java-Spring based web application for seamless team collaboration.
•Managed SageMaker training jobs, optimizing model performance through distributed training on multiple GPU instances, significantly reducing training time and cost.
•Integrated with GraphQL to provide dynamic query capabilities to clients.
•Built and maintained scalable enterprise-grade web applications using .NET Core for backend APIs and React for dynamic, user-friendly frontends.
•Developed a comprehensive e-commerce platform with .NET for order management and React for interactive customer interfaces.
•Developed a healthcare appointment scheduling system using .NET for backend logic and React for a responsive user interface.


Education
NOVEMBER 2015 - AUGUST 2017
Master's degree, Computer Science | Texas A&M University | College Station, TX


SEPTEMBER 2011 - OCTOBER 2015
Bachelor's degree, Computer Science | Texas A&M University | College Station, TX


Licenses & Certifications
- Python Essentials 2 
- Javascript Essentials 2 
CONTACT:
- Email: realtopman2026@outlook.com
- Phone: (561) 570-6455
- Address: 280 W Faust St, New Braunfels, TX 78130
- LinkedIn: linkedin.com/in/everestcarter3/
- GitHub: github.com/realtopman2026
- Portfolio: everestcarter03.github.io

GUIDELINES:
- Be conversational, friendly, and professional
- Answer questions about Everest's background, skills, experience, projects, and education
- If asked something outside the portfolio, politely redirect to portfolio topics
- Keep responses concise but informative
- Refer to Everest in third person (e.g. "Everest has experience in...")
- If you don't know something specific, say so honestly
"""
        super().__init__(
            name="ResponseAgent",
            system_prompt=system_prompt,
            temperature=0.7
        )
        self.portfolio_data = self._load_portfolio_data()

    def _load_portfolio_data(self) -> Dict[str, Any]:
        """Load local portfolio data for offline fallback responses."""
        data_path = Path(__file__).resolve().parents[3] / "data" / "sample_portfolio_data.json"
        try:
            with open(data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _contains_any(self, query: str, terms: list[str]) -> bool:
        """Match whole words/phrases to avoid accidental substring hits."""
        return any(re.search(rf"\b{re.escape(term)}\b", query) for term in terms)

    def _should_answer_locally(self, user_input: str) -> bool:
        """Use local portfolio data for common site-chat questions."""
        query = user_input.lower()
        local_tokens = [
            "hello", "hi", "hey", "good morning", "good evening",
            "who are you", "who is everest", "tell me about yourself", "tell me about everest",
            "project", "free flow", "portfolio copilot", "built",
            "skill", "skills", "tech", "stack", "language", "framework",
            "experience", "work", "company", "intern", "job",
            "education", "degree", "university", "gpa", "study",
            "contact", "email", "linkedin", "github", "reach",
            "phone", "cell", "number", "call", "address", "location",
            "visa", "opt", "sponsorship", "stem extension", "work authorization",
        ]
        return self._contains_any(query, local_tokens)

    def _fallback_response(self, user_input: str) -> str:
        """Generate a deterministic response when LLM calls fail."""
        query = user_input.lower()
        data = self.portfolio_data or {}
        name = data.get("name", "Everest Carter")
        contact = data.get("contact", {})
        projects = data.get("projects", [])
        experience = data.get("experience", [])
        education = data.get("education", [])
        skills = data.get("skills", {})

        def format_experience(company_query: str) -> Optional[str]:
            for exp in experience:
                company_name = exp.get("company", "")
                if company_query in company_name.lower():
                    highlights = exp.get("highlights", [])
                    role = exp.get("role", "Role")
                    duration = exp.get("duration", "Duration")
                    lines = [f"{role} at {company_name} ({duration})"]
                    for h in highlights[:4]:
                        lines.append(f"- {h}")
                    return "\n".join(lines)
            return None

        def format_projects() -> str:
            if not projects:
                return "No projects found."
            lines = []
            for project in projects:
                name_line = project.get("name", "Project")
                desc = project.get("description", "")
                features = project.get("features", [])
                links = project.get("links", {})
                lines.append(name_line)
                if desc:
                    lines.append(f"  • {desc}")
                if features:
                    for f in features[:4]:
                        lines.append(f"  - {f}")
                if links:
                    for label, url in links.items():
                        lines.append(f"  - {label.title()} link: {url}")
                lines.append("")
            return "\n".join(lines).strip()

        def format_skills() -> str:
            if not skills:
                return "No skills found."
            ordered = [
                ("Programming Languages", skills.get("programming_languages", [])),
                ("Frameworks", skills.get("frameworks", [])),
                ("Cloud/DevOps", skills.get("cloud_devops", [])),
                ("Databases", skills.get("databases", [])),
                ("Mobile", skills.get("mobile_development", [])),
                ("Tools/Practices", skills.get("tools_practices", [])),
            ]
            lines = []
            for label, items in ordered:
                if items:
                    lines.append(f"{label}: {', '.join(items)}")
            return "\n".join(lines)

        if self._contains_any(query, ["hello", "hi", "hey", "good morning", "good evening"]):
            return (
                f"Hi, I'm the portfolio copilot for {name}. "
                "You can ask about projects, skills, experience, education, or contact details."
            )

        if self._contains_any(query, ["linkedin"]):
            return (
                f"You can view {name}'s LinkedIn here:\n"
                f"{contact.get('linkedin', 'N/A')}"
            )

        if self._contains_any(query, ["github"]):
            return (
                f"You can view {name}'s GitHub here:\n"
                f"{contact.get('github', 'N/A')}"
            )

        if self._contains_any(query, ["portfolio"]) and not self._contains_any(query, ["portfolio copilot", "project"]):
            return (
                f"You can view {name}'s portfolio here:\n"
                f"{contact.get('portfolio', data.get('portfolio_url', 'N/A'))}"
            )

        if self._contains_any(query, ["email", "mail"]):
            return (
                f"You can reach {name} by email here:\n"
                f"{contact.get('email', 'N/A')}"
            )

        if self._contains_any(query, ["phone", "cell", "number", "call"]):
            return (
                f"You can reach {name} by phone here:\n"
                f"{contact.get('phone', 'N/A')}"
            )

        if self._contains_any(query, ["address", "location", "where are you located", "where are you based"]):
            return (
                f"{name}'s address is:\n"
                f"{contact.get('address', 'N/A')}"
            )

        if self._contains_any(query, ["visa", "opt", "work authorization"]):
            return (
                f"{name}'s visa status is:\n"
                f"{contact.get('visa_status', 'N/A')}"
            )

        if self._contains_any(query, ["sponsorship", "stem extension"]):
            return (
                f"Sponsorship details for {name}:\n"
                f"{contact.get('sponsorship', 'N/A')}"
            )

        cerence_exp = format_experience("cerence")
        iconsult_exp = format_experience("iconsult")
        if self._contains_any(query, ["cerence", "cerence ai"]) and cerence_exp:
            return cerence_exp
        if self._contains_any(query, ["iconsult", "iconsult collaborative", "yoga4philly"]) and iconsult_exp:
            return iconsult_exp

        if self._contains_any(query, ["project", "portfolio copilot", "free flow", "built"]):
            return format_projects()

        if self._contains_any(query, ["skill", "skills", "tech", "stack", "language", "framework"]):
            return format_skills()

        if self._contains_any(query, ["contact", "email", "linkedin", "github", "reach"]):
            return (
                f"You can contact {name} here:\n"
                f"- Email: {contact.get('email', 'N/A')}\n"
                f"- Phone: {contact.get('phone', 'N/A')}\n"
                f"- Address: {contact.get('address', 'N/A')}\n"
                f"- Visa Status: {contact.get('visa_status', 'N/A')}\n"
                f"- Sponsorship: {contact.get('sponsorship', 'N/A')}\n"
                f"- LinkedIn: {contact.get('linkedin', 'N/A')}\n"
                f"- GitHub: {contact.get('github', 'N/A')}\n"
                f"- Portfolio: {contact.get('portfolio', data.get('portfolio_url', 'N/A'))}"
            )

        if self._contains_any(query, ["experience", "work", "company", "intern"]):
            lines = [f"{name}'s experience:"]
            for exp in experience[:3]:
                lines.append(f"- {exp.get('role', 'Role')} at {exp.get('company', 'Company')} ({exp.get('duration', 'N/A')})")
            return "\n".join(lines)

        if self._contains_any(query, ["education", "degree", "university", "gpa", "study"]):
            lines = [f"{name}'s education:"]
            for edu in education:
                lines.append(
                    f"- {edu.get('degree', 'Degree')} at {edu.get('institution', 'Institution')} "
                    f"({edu.get('graduation', 'N/A')}, GPA {edu.get('gpa', 'N/A')})"
                )
            return "\n".join(lines)

        return (
            f"{name} is a {data.get('title', 'Software Engineer')} with {data.get('stats', {}).get('years_experience', '8+')} years of experience, "
            f"and has built {data.get('stats', {}).get('projects_built', '10+')} projects. "
            f"You can ask about projects, skills, experience, education, or contact details."
        )

    def _context_fallback_response(self, formatted_context: str) -> str:
        """Return retrieved document context when LLM generation is unavailable."""
        cleaned = re.sub(r"\n{3,}", "\n\n", formatted_context).strip()
        if len(cleaned) > 1400:
            cleaned = cleaned[:1400].rsplit(" ", 1)[0].rstrip() + "..."
        return f"I found this in the ingested knowledge base:\n\n{cleaned}"
    
    def process(self, user_input: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """Generate response based on query and retrieved context."""
        print("process")
        
        if self._should_answer_locally(user_input):
            print("_should_answer_locally")
            response_text = self._fallback_response(user_input)
            self.add_to_history(user_input, response_text)
            return {
                "agent": self.name,
                "response": response_text,
                "query": user_input,
                "used_context": False,
                "success": True,
                "fallback_used": True,
            }

        if context and context.get("formatted_context"):
            prompt = f"""User Query: {user_input}

Additional Retrieved Context:
{context['formatted_context']}

Generate a helpful response about Everest based on the query and any additional context above."""
        else:
            prompt = f"""User Query: {user_input}

Generate a helpful response about Everest based on the query. Use the portfolio information from your system prompt."""
        
        messages = self._build_messages(prompt)
        
        try:
            print("invoking_llm")
            response = self._invoke_llm(messages)
            response_text = response.content
            
            self.add_to_history(user_input, response_text)
            
            return {
                "agent": self.name,
                "response": response_text,
                "query": user_input,
                "used_context": bool(context and context.get("formatted_context")),
                "success": True
            }
        except Exception as e:
            fallback = (
                self._context_fallback_response(context["formatted_context"])
                if context and context.get("formatted_context")
                else self._fallback_response(user_input)
            )
            return {
                "agent": self.name,
                "response": fallback,
                "query": user_input,
                "success": True,
                "fallback_used": True,
                "error": str(e)
            }
