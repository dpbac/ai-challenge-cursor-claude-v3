import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="AI Personal Challenge",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'quiz'
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}

# Quiz questions
questions = [
    {
        "id": 1,
        "question": "Which of these general areas are you most interested in? (Select up to 3)",
        "options": [
            "Environment and sustainability",
            "Business and commerce",
            "Healthcare and medicine",
            "Education and learning",
            "Media and entertainment",
            "Transportation and logistics",
            "Arts and creativity",
            "Social impact and ethics",
            "Finance and economics",
            "Agriculture and food systems",
            "Internet of Things and smart devices",
            "Remote work and collaboration",
            "Analytics and business intelligence",
            "Security and privacy",
            "Climate change and renewable energy"
        ],
        "max_selections": 3,
        "type": "checkbox"
    },
    {
        "id": 2,
        "question": "What type of data are you most excited to work with? (Select up to 2)",
        "options": [
            "Numbers and statistics",
            "Text and language",
            "Images and visual content",
            "Audio and sound",
            "Time-based data (sequences, predictions)",
            "Geographic and location data",
            "User behavior and interactions",
            "Sensor and IoT data",
            "Financial transactions",
            "Medical and health records"
        ],
        "max_selections": 2,
        "type": "checkbox"
    },
    {
        "id": 3,
        "question": "Which aspects of AI technology interest you most? (Select up to 3)",
        "options": [
            "Making predictions about future events",
            "Finding patterns and grouping similar items",
            "Creating personalized recommendations",
            "Recognizing objects or concepts in images",
            "Understanding and generating human language",
            "Optimizing processes and decisions",
            "Creating new content (text, images, music)",
            "Making systems more explainable and transparent",
            "Ensuring fairness and reducing bias",
            "Conversational interfaces and dialogue systems",
            "Computer vision and image understanding",
            "Anomaly detection and fraud prevention"
        ],
        "max_selections": 3,
        "type": "checkbox"
    },
    {
        "id": 4,
        "question": "What skills would you most like to develop during this project? (Select up to 3)",
        "options": [
            "Data collection and preparation",
            "Statistical analysis",
            "Programming and coding",
            "Model selection and training",
            "Evaluation and testing",
            "Visualization and communication",
            "Ethical considerations and impact assessment",
            "Project management",
            "Domain knowledge in a specific field",
            "Deploying models in real-world settings",
            "Working with large language models",
            "Optimizing AI systems for performance or efficiency"
        ],
        "max_selections": 3,
        "type": "checkbox"
    },
    {
        "id": 5,
        "question": "What's your current experience level with AI/ML? (Select one)",
        "options": [
            "Complete beginner",
            "Some theoretical knowledge",
            "Basic practical experience",
            "Intermediate experience",
            "Advanced experience in specific areas"
        ],
        "max_selections": 1,
        "type": "radio"
    },
    {
        "id": 6,
        "question": "How do you prefer to approach learning? (Select one)",
        "options": [
            "Starting with theory and then applying it",
            "Learning by doing and experimenting",
            "Solving specific problems",
            "Exploring openly without a fixed goal"
        ],
        "max_selections": 1,
        "type": "radio"
    },
    {
        "id": 7,
        "question": "Which AI Explorations themes have you already worked with? (Select all that apply)",
        "options": [
            "Green AI & Environment",
            "AI for Business & Marketing",
            "AI for Health & Medicine",
            "AI for Data Analysis & Decision Support",
            "AI in Education",
            "AI in Retail & E-commerce",
            "AI in Media & Communication",
            "AI for Visual Understanding & Computer Vision",
            "Responsible AI & Model Explainability",
            "AI for Security & Spam Detection",
            "AI for Climate Change & Sustainability",
            "AI in Finance & Fintech",
            "AI for Social Good",
            "AI in Transportation & Logistics",
            "AI Ethics & Governance",
            "AI in Creative Arts",
            "AI for Remote Work & Collaboration",
            "AI in Agriculture",
            "AI for Internet of Things (IoT)",
            "Conversational AI & Agents",
            "AI for Analytics & Business Intelligence",
            "None of the above / I'm just starting with AI Explorations"
        ],
        "max_selections": None,
        "type": "checkbox"
    },
    {
        "id": 8,
        "question": "For your Personal AI Quest, would you prefer to: (Select one)",
        "options": [
            "Explore a completely different area from my AI Explorations",
            "Deepen my knowledge in one of my previous AI Explorations themes",
            "Build upon a specific AI Exploration project I've already started",
            "Work in a related but distinct field from my previous AI Explorations",
            "Not sure yet"
        ],
        "max_selections": 1,
        "type": "radio"
    },
    {
        "id": 9,
        "question": "What timeframe are you considering for your Personal AI Quest within the 15-week semester? (Select one)",
        "options": [
            "A compact project I can complete in 2-3 weeks",
            "A medium-sized project spanning 4-7 weeks",
            "An ambitious project I'll work on for 8-15 weeks (most/all of the semester)",
            "Not sure yet"
        ],
        "max_selections": 1,
        "type": "radio"
    },
    {
        "id": 10,
        "question": "What kind of impact would you like your AI project to have? (Select up to 2)",
        "options": [
            "Help people in their daily lives",
            "Improve business processes or decisions",
            "Address environmental or climate challenges",
            "Enhance learning or education",
            "Create new artistic or creative possibilities",
            "Promote fairness, transparency, or ethics",
            "Explore new technical capabilities",
            "Solve an interesting intellectual challenge",
            "Support healthcare or medical applications",
            "Improve agricultural or food systems"
        ],
        "max_selections": 2,
        "type": "checkbox"
    },
    {
        "id": 11,
        "question": "What resources do you already have or can easily access for your project? (Select all that apply)",
        "options": [
            "Specific datasets",
            "Programming skills in Python",
            "Experience with ML libraries (TensorFlow, PyTorch, scikit-learn, etc.)",
            "Domain knowledge in a specific field",
            "Connections to potential users or stakeholders",
            "Access to specialized hardware (GPU, etc.)",
            "Experience with large language models or generative AI",
            "None of the above / Not sure"
        ],
        "max_selections": None,
        "type": "checkbox"
    },
    {
        "id": 12,
        "question": "How comfortable are you with these aspects of AI development? (Rate from 1-5: 1 = Not comfortable, 5 = Very comfortable)",
        "options": [
            "Data cleaning and preprocessing",
            "Model selection and training",
            "Evaluating model performance",
            "Interpreting results",
            "Ethical considerations",
            "Working with computer vision",
            "Natural language processing",
            "Time series analysis"
        ],
        "type": "rating",
        "max_selections": 1
    },
    {
        "id": 13,
        "question": "Which of these specific AI application areas most interest you? (Select up to 3)",
        "options": [
            "Green AI & Environmental monitoring",
            "Business analytics and marketing optimization",
            "Healthcare diagnostics and patient care",
            "Educational technology and learning analytics",
            "Media content analysis and generation",
            "Visual understanding and computer vision",
            "Model explainability and responsible AI",
            "Cybersecurity and threat detection",
            "Climate modeling and sustainability",
            "Financial forecasting and risk analysis",
            "Social good and humanitarian applications",
            "Transportation optimization and logistics",
            "Creative applications in art and music",
            "Remote work tools and collaboration",
            "Agricultural monitoring and optimization",
            "Smart homes and IoT applications",
            "Conversational agents and chatbots",
            "Business intelligence dashboards"
        ],
        "max_selections": 3,
        "type": "checkbox"
    },
    {
        "id": 14,
        "question": "Which AI research questions from our thematic groupings resonate most with you? (Select up to 3)",
        "options": [
            "Predicting environmental patterns (weather, energy usage, etc.)",
            "Analyzing customer behavior and preferences",
            "Detecting health conditions from medical data",
            "Understanding educational patterns and personalization",
            "Processing and generating media content",
            "Recognizing and analyzing visual information",
            "Explaining AI decisions and ensuring fairness",
            "Detecting anomalies and security threats",
            "Modeling climate impacts and sustainability",
            "Forecasting financial markets and detecting fraud",
            "Supporting humanitarian and social good initiatives",
            "Optimizing transportation and delivery networks",
            "Generating creative content and art",
            "Enhancing remote collaboration and productivity",
            "Improving agricultural yields and sustainability",
            "Connecting and optimizing IoT devices",
            "Building better conversational systems",
            "Creating actionable business insights"
        ],
        "max_selections": 3,
        "type": "checkbox"
    }
]

# Topic recommendations based on quiz answers
topic_recommendations = {
    "Machine Learning and Data Science": {
        "prompt": "Let's explore machine learning applications in [specific domain]. What are some innovative ways we can apply ML techniques to solve real-world problems in this area?",
        "description": "Focus on developing and implementing machine learning models for practical applications."
    },
    "Natural Language Processing": {
        "prompt": "How can we leverage NLP to improve [specific application]? Let's discuss potential approaches and challenges in implementing language models.",
        "description": "Explore the development of language processing systems and their applications."
    },
    "Computer Vision": {
        "prompt": "What are the current challenges and opportunities in computer vision for [specific use case]? Let's brainstorm innovative solutions.",
        "description": "Investigate image processing and computer vision applications."
    },
    "Robotics and Automation": {
        "prompt": "How can we enhance automation in [specific industry] using AI? Let's discuss the integration of AI with robotic systems.",
        "description": "Focus on AI applications in robotics and automation systems."
    },
    "Ethics and Social Impact": {
        "prompt": "What are the ethical implications of AI in [specific context]? Let's analyze the social impact and potential solutions.",
        "description": "Examine the ethical considerations and societal impact of AI technologies."
    }
}

def show_quiz():
    st.title("AI Interest Quiz for Personal AI Quest")
    st.write("This quiz will help you discover AI topics that might interest you for your Personal AI Quest. Your answers will generate a personalized profile showing which AI domains align with your interests, skills, and goals.")
    st.write("Remember, this is just to inspire you - the final choice of topic and research question is yours!")

    for question in questions:
        st.subheader(f"Question {question['id']}: {question['question']}")
        
        if question.get('type') == 'text':
            answer = st.text_area("Your answer:", key=f"q{question['id']}")
            st.session_state.quiz_answers[question["id"]] = answer
        elif question.get('type') == 'rating':
            for option in question['options']:
                rating = st.slider(option, 1, 5, 3, key=f"q{question['id']}_{option}")
                if question["id"] not in st.session_state.quiz_answers:
                    st.session_state.quiz_answers[question["id"]] = {}
                st.session_state.quiz_answers[question["id"]][option] = rating
        else:
            # Create a grid of checkboxes or radio buttons based on question type
            cols = st.columns(2)
            selected = []
            
            if question['type'] == 'radio':
                # For radio buttons, we don't need columns
                answer = st.radio(
                    "Select your answer:",
                    question["options"],
                    key=f"q{question['id']}",
                    index=None
                )
                st.session_state.quiz_answers[question["id"]] = answer
            else:  # checkbox type
                for i, option in enumerate(question['options']):
                    col = cols[i % 2]
                    if col.checkbox(option, key=f"q{question['id']}_{i}"):
                        selected.append(option)
                
                # Limit selections to max_selections if specified
                if question['max_selections'] and len(selected) > question['max_selections']:
                    st.warning(f"Please select no more than {question['max_selections']} options")
                    # Remove the last selected option
                    selected = selected[:-1]
                
                st.session_state.quiz_answers[question["id"]] = selected
    
    if st.button("Get Recommendations"):
        # Check if all required questions are answered
        all_answered = True
        for question in questions:
            if question["id"] not in st.session_state.quiz_answers:
                all_answered = False
                break
            if isinstance(st.session_state.quiz_answers[question["id"]], list):
                if question.get('max_selections') and len(st.session_state.quiz_answers[question["id"]]) < 1:
                    all_answered = False
                    break
        
        if all_answered:
            st.session_state.current_page = 'results'
            st.rerun()
        else:
            st.error("Please answer all questions before proceeding.")

def show_results():
    st.title("Your Personal AI Quest Recommendation")
    
    # Get all quiz answers
    interests = st.session_state.quiz_answers[1]  # Selected interests from Q1
    data_types = st.session_state.quiz_answers[2]  # Data types from Q2
    ai_aspects = st.session_state.quiz_answers[3]  # AI aspects from Q3
    skills = st.session_state.quiz_answers[4]  # Skills from Q4
    experience = st.session_state.quiz_answers[5]  # Experience level from Q5
    learning_style = st.session_state.quiz_answers[6]  # Learning style from Q6
    timeframe = st.session_state.quiz_answers[9]  # Timeframe from Q9
    impact = st.session_state.quiz_answers[10]  # Impact from Q10
    resources = st.session_state.quiz_answers[11]  # Resources from Q11
    
    # Define topic categories and their related aspects
    topic_categories = {
        "Environment and sustainability": {
            "data_types": ["Numbers and statistics", "Geographic and location data", "Sensor and IoT data"],
            "ai_aspects": ["Making predictions about future events", "Finding patterns and grouping similar items", "Optimizing processes and decisions"],
            "skills": ["Data collection and preparation", "Statistical analysis", "Model selection and training"],
            "impact": ["Address environmental or climate challenges", "Help people in their daily lives"]
        },
        "Business and commerce": {
            "data_types": ["Numbers and statistics", "User behavior and interactions", "Financial transactions"],
            "ai_aspects": ["Creating personalized recommendations", "Optimizing processes and decisions", "Making predictions about future events"],
            "skills": ["Statistical analysis", "Programming and coding", "Project management"],
            "impact": ["Improve business processes or decisions", "Solve an interesting intellectual challenge"]
        },
        "Healthcare and medicine": {
            "data_types": ["Numbers and statistics", "Medical and health records", "Images and visual content"],
            "ai_aspects": ["Making predictions about future events", "Recognizing objects or concepts in images", "Finding patterns and grouping similar items"],
            "skills": ["Data collection and preparation", "Model selection and training", "Evaluation and testing"],
            "impact": ["Support healthcare or medical applications", "Help people in their daily lives"]
        },
        "Education and learning": {
            "data_types": ["Text and language", "User behavior and interactions", "Time-based data"],
            "ai_aspects": ["Understanding and generating human language", "Creating personalized recommendations", "Making systems more explainable and transparent"],
            "skills": ["Programming and coding", "Visualization and communication", "Ethical considerations and impact assessment"],
            "impact": ["Enhance learning or education", "Help people in their daily lives"]
        },
        "Media and entertainment": {
            "data_types": ["Text and language", "Images and visual content", "Audio and sound"],
            "ai_aspects": ["Creating new content", "Understanding and generating human language", "Recognizing objects or concepts in images"],
            "skills": ["Programming and coding", "Model selection and training", "Visualization and communication"],
            "impact": ["Create new artistic or creative possibilities", "Explore new technical capabilities"]
        },
        "Transportation and logistics": {
            "data_types": ["Numbers and statistics", "Geographic and location data", "Time-based data"],
            "ai_aspects": ["Optimizing processes and decisions", "Making predictions about future events", "Finding patterns and grouping similar items"],
            "skills": ["Data analysis", "Model selection and training", "Project management"],
            "impact": ["Improve business processes or decisions", "Help people in their daily lives"]
        },
        "Arts and creativity": {
            "data_types": ["Images and visual content", "Audio and sound", "Text and language"],
            "ai_aspects": ["Creating new content", "Understanding and generating human language", "Recognizing objects or concepts in images"],
            "skills": ["Programming and coding", "Model selection and training", "Visualization and communication"],
            "impact": ["Create new artistic or creative possibilities", "Explore new technical capabilities"]
        },
        "Social impact and ethics": {
            "data_types": ["Text and language", "User behavior and interactions", "Numbers and statistics"],
            "ai_aspects": ["Making systems more explainable and transparent", "Ensuring fairness and reducing bias", "Understanding and generating human language"],
            "skills": ["Ethical considerations and impact assessment", "Data analysis", "Visualization and communication"],
            "impact": ["Promote fairness, transparency, or ethics", "Help people in their daily lives"]
        },
        "Finance and economics": {
            "data_types": ["Numbers and statistics", "Financial transactions", "Time-based data"],
            "ai_aspects": ["Making predictions about future events", "Finding patterns and grouping similar items", "Optimizing processes and decisions"],
            "skills": ["Statistical analysis", "Programming and coding", "Model selection and training"],
            "impact": ["Improve business processes or decisions", "Solve an interesting intellectual challenge"]
        },
        "Agriculture and food systems": {
            "data_types": ["Numbers and statistics", "Sensor and IoT data", "Geographic and location data"],
            "ai_aspects": ["Making predictions about future events", "Finding patterns and grouping similar items", "Optimizing processes and decisions"],
            "skills": ["Data collection and preparation", "Statistical analysis", "Model selection and training"],
            "impact": ["Improve agricultural or food systems", "Help people in their daily lives"]
        },
        "Internet of Things and smart devices": {
            "data_types": ["Sensor and IoT data", "Numbers and statistics", "Time-based data"],
            "ai_aspects": ["Making predictions about future events", "Finding patterns and grouping similar items", "Optimizing processes and decisions"],
            "skills": ["Data collection and preparation", "Programming and coding", "Model selection and training"],
            "impact": ["Help people in their daily lives", "Explore new technical capabilities"]
        },
        "Remote work and collaboration": {
            "data_types": ["User behavior and interactions", "Text and language", "Time-based data"],
            "ai_aspects": ["Understanding and generating human language", "Creating personalized recommendations", "Making systems more explainable and transparent"],
            "skills": ["Programming and coding", "Project management", "Visualization and communication"],
            "impact": ["Help people in their daily lives", "Improve business processes or decisions"]
        },
        "Analytics and business intelligence": {
            "data_types": ["Numbers and statistics", "User behavior and interactions", "Time-based data"],
            "ai_aspects": ["Making predictions about future events", "Finding patterns and grouping similar items", "Creating personalized recommendations"],
            "skills": ["Statistical analysis", "Programming and coding", "Data analysis"],
            "impact": ["Improve business processes or decisions", "Solve an interesting intellectual challenge"]
        },
        "Security and privacy": {
            "data_types": ["Numbers and statistics", "Text and language", "User behavior and interactions"],
            "ai_aspects": ["Finding patterns and grouping similar items", "Making systems more explainable and transparent", "Ensuring fairness and reducing bias"],
            "skills": ["Data analysis", "Programming and coding", "Ethical considerations and impact assessment"],
            "impact": ["Promote fairness, transparency, or ethics", "Help people in their daily lives"]
        },
        "Climate change and renewable energy": {
            "data_types": ["Numbers and statistics", "Geographic and location data", "Sensor and IoT data"],
            "ai_aspects": ["Making predictions about future events", "Finding patterns and grouping similar items", "Optimizing processes and decisions"],
            "skills": ["Data collection and preparation", "Statistical analysis", "Model selection and training"],
            "impact": ["Address environmental or climate challenges", "Help people in their daily lives"]
        }
    }
    
    # Calculate match scores for each topic
    topic_matches = []
    for topic, category in topic_categories.items():
        # Calculate match score based on various factors
        match_score = 0
        
        # 1. Primary Interest (40 points max)
        if topic in interests:
            match_score += 40  # Base score for selected interest
            # Bonus for being in top 3 selected interests
            if interests.index(topic) < 3:
                match_score += 10
        
        # 2. Data Types Alignment (20 points max)
        data_type_matches = sum(1 for dt in data_types if dt in category["data_types"])
        match_score += data_type_matches * 5  # 5 points per matching data type
        
        # 3. AI Aspects Alignment (20 points max)
        aspect_matches = sum(1 for aspect in ai_aspects if aspect in category["ai_aspects"])
        match_score += aspect_matches * 5  # 5 points per matching aspect
        
        # 4. Skills Alignment (20 points max)
        skill_matches = sum(1 for skill in skills if skill in category["skills"])
        match_score += skill_matches * 5  # 5 points per matching skill
        
        # 5. Impact Alignment (15 points max)
        impact_matches = sum(1 for imp in impact if imp in category["impact"])
        match_score += impact_matches * 5  # 5 points per matching impact
        
        # 6. Experience Level Bonus (10 points max)
        if experience == "Advanced experience in specific areas":
            match_score += 10
        elif experience == "Intermediate experience":
            match_score += 5
        
        # 7. Learning Style Bonus (10 points max)
        if learning_style == "Learning by doing and experimenting":
            match_score += 10
        elif learning_style == "Solving specific problems":
            match_score += 5
        
        # 8. Timeframe Alignment (10 points max)
        if timeframe == "An ambitious project I'll work on for 8-15 weeks":
            match_score += 10
        elif timeframe == "A medium-sized project spanning 4-7 weeks":
            match_score += 5
        
        # 9. Resources Bonus (10 points max)
        resource_bonus = 0
        if "Programming skills in Python" in resources:
            resource_bonus += 3
        if "Experience with ML libraries" in resources:
            resource_bonus += 3
        if "Specific datasets" in resources:
            resource_bonus += 2
        if "Domain knowledge in a specific field" in resources:
            resource_bonus += 2
        match_score += min(resource_bonus, 10)
        
        # 10. Previous Experience Bonus (10 points max)
        if any(theme in st.session_state.quiz_answers[7] for theme in [
            "Green AI & Environment", "AI for Business & Marketing", "AI for Health & Medicine",
            "AI for Data Analysis & Decision Support", "AI in Education", "AI in Retail & E-commerce",
            "AI in Media & Communication", "AI for Visual Understanding & Computer Vision",
            "Responsible AI & Model Explainability", "AI for Security & Spam Detection",
            "AI for Climate Change & Sustainability", "AI in Finance & Fintech",
            "AI for Social Good", "AI in Transportation & Logistics", "AI Ethics & Governance",
            "AI in Creative Arts", "AI for Remote Work & Collaboration", "AI in Agriculture",
            "AI for Internet of Things (IoT)", "Conversational AI & Agents",
            "AI for Analytics & Business Intelligence"
        ]):
            match_score += 10
        
        # Add topic to matches with normalized score (0-100)
        normalized_score = min(100, match_score)
        topic_matches.append({
            "name": topic,
            "match": normalized_score,
            "overview": f"This area focuses on applying AI to {topic.lower()}. You'll explore how artificial intelligence can be used to address challenges and create opportunities in this domain.",
            "directions": [
                f"Analyzing {topic.lower()} data and patterns",
                f"Developing AI solutions for {topic.lower()} challenges",
                f"Exploring ethical implications of AI in {topic.lower()}"
            ],
            "datasets": [
                f"Public datasets related to {topic.lower()}",
                "Kaggle datasets in this domain",
                "Open data sources from relevant organizations"
            ],
            "techniques": [
                "Machine Learning algorithms",
                "Data analysis and visualization",
                "Model evaluation and optimization"
            ],
            "outcomes": [
                f"Understanding AI applications in {topic.lower()}",
                "Developing domain-specific AI solutions",
                "Evaluating impact and effectiveness"
            ]
        })
    
    # Sort topics by match score and get top 3
    topic_matches.sort(key=lambda x: x["match"], reverse=True)
    top_topics = topic_matches[:3]
    
    # Display interest profile
    st.subheader("Your Interest Profile")
    st.write("Based on your responses, here are your top AI interest areas:")
    
    # Display match percentages
    for i, topic in enumerate(top_topics, 1):
        st.write(f"{i}. {topic['name']} - {topic['match']}% match")
    
    st.write("\nLet's explore these areas to help you formulate your own research question!")
    
    # Display detailed information for each topic
    for topic in top_topics:
        with st.expander(f"{topic['name']}", expanded=(topic == top_topics[0])):
            st.subheader("Overview")
            st.write(topic['overview'])
            
            st.subheader("Why This Matches Your Interests")
            st.write(f"Your quiz responses showed strong alignment with this area based on your interests, skills, and goals.")
            
            st.subheader("Inspiration for Research Questions")
            st.write("While you'll develop your own specific research question, here are some directions to consider:")
            for direction in topic['directions']:
                st.write(f"• {direction}")
            
            st.subheader("Potential Datasets")
            for dataset in topic['datasets']:
                st.write(f"• {dataset}")
            
            st.subheader("Techniques You Might Explore")
            for technique in topic['techniques']:
                st.write(f"• {technique}")
            
            st.subheader("Learning Outcome Connections")
            st.write("This topic area particularly supports these learning outcomes from the AI Basics semester:")
            for outcome in topic['outcomes']:
                st.write(f"• {outcome}")
    
    # Topic selection buttons
    st.subheader("Choose Your Topic")
    st.write("Select one of the topics above to get a customized AI conversation prompt:")
    
    cols = st.columns(3)
    for i, topic in enumerate(top_topics):
        with cols[i]:
            if st.button(topic['name']):
                st.session_state.selected_topic = topic
    
    # Display AI conversation prompt when a topic is selected
    if 'selected_topic' in st.session_state:
        st.subheader("AI Conversation Prompt for Your Personal AI Quest")
        st.write("Below is a customized prompt based on your quiz results. Copy and paste this into a conversation with Claude or another AI assistant to explore your topic further.")
        
        prompt = f"""Prompt for {st.session_state.selected_topic['name']}:

Hi Claude! I'm a student working on my Personal AI Quest for an AI Basics semester. Based on my interests, I've identified {st.session_state.selected_topic['name']} as a potential focus area.

My Background and Interests:
• I'm interested in working with these types of data: {', '.join(data_types)}
• The aspects of AI that interest me most are: {', '.join(ai_aspects)}
• My current experience level with AI is: {experience}
• I have approximately {timeframe} to complete this project
• I already have some knowledge/resources in: {', '.join(resources) if resources else 'None specified'}

What I'd Like Help With:
1. Could you suggest 3-5 interesting and achievable applications of AI in {st.session_state.selected_topic['name']} that match my interests?
2. For each application, what kinds of datasets might be available or useful?
3. What specific AI techniques would be most relevant for these applications?
4. How might I scope a project that's challenging but achievable in my timeframe?
5. What ethical considerations should I be aware of in this area?
6. What are some common pitfalls or challenges I might encounter?

I'm looking to use this conversation to help me formulate my own research question, so I'd appreciate diverse suggestions rather than a single recommendation.

Thank you for your help!

Note: After your conversation, remember to save any insights that help you formulate your research question. Your next step will be to define your specific research question and complete your project plan."""

        st.code(prompt, language="text")
        
        # Add button to proceed to project plan
        if st.button("Create Project Plan"):
            st.session_state.current_page = 'project_plan'
            st.rerun()

def show_project_plan():
    st.title("Project Plan")
    
    # Get the selected topic from session state
    selected_topic = st.session_state.get('selected_topic', {'name': 'Not Selected'})
    
    # Project plan form
    with st.form("project_plan_form"):
        st.subheader("Basic Information")
        name = st.text_input("Your Name")
        date = st.date_input("Date")
        topic_area = st.text_input("Topic Area", value=selected_topic['name'])
        
        st.subheader("Project Definition")
        research_question = st.text_area("Research Question")
        personal_motivation = st.text_area("Personal Motivation")
        
        st.subheader("Connection to Learning Outcomes")
        learning_outcomes = st.multiselect(
            "Select relevant learning outcomes:",
            [
                "Analyzing data for AI models",
                "Advising on ethical/social impact",
                "Designing AI solutions",
                "Implementing AI models",
                "Monitoring AI performance"
            ]
        )
        
        st.subheader("Methodology")
        st.write("Data")
        data_sources = st.text_area("Data Source(s)")
        data_preparation = st.text_area("Data Preparation")
        ethical_considerations = st.text_area("Ethical Considerations")
        
        st.write("AI Approach")
        techniques_models = st.text_area("Techniques/Models")
        implementation_tools = st.text_area("Implementation Tools")
        evaluation_method = st.text_area("Evaluation Method")
        
        st.subheader("Project Planning")
        st.write("Timeline")
        weeks = 5
        timeline = []
        for week in range(1, weeks + 1):
            activities = st.text_area(f"Week {week} Activities")
            deliverables = st.text_area(f"Week {week} Deliverables")
            timeline.append({
                "week": week,
                "activities": activities,
                "deliverables": deliverables
            })
        
        resources_needed = st.text_area("Resources Needed")
        potential_challenges = st.text_area("Potential Challenges")
        
        st.subheader("Documentation & Presentation")
        documentation_plan = st.text_area("Documentation Plan")
        presentation_format = st.text_area("Presentation Format")
        
        submitted = st.form_submit_button("Generate Project Plan")
        
        if submitted:
            # Create the project plan template
            project_plan = f"""Personal AI Quest Project Plan

Basic Information
• Name: {name}
• Date: {date}
• Topic Area: {topic_area}

Project Definition
Research Question
{research_question}

Personal Motivation
{personal_motivation}

Connection to Learning Outcomes
This project will help me achieve the following learning outcomes from the AI Basics semester:
{chr(10).join([f"• {outcome}" for outcome in learning_outcomes])}

Methodology
Data
• Data Source(s): {data_sources}
• Data Preparation: {data_preparation}
• Ethical Considerations: {ethical_considerations}

AI Approach
• Techniques/Models: {techniques_models}
• Implementation Tools: {implementation_tools}
• Evaluation Method: {evaluation_method}

Project Planning
Timeline
Week\tActivities\tDeliverables
{chr(10).join([f"{week['week']}\t{week['activities']}\t{week['deliverables']}" for week in timeline])}

Resources Needed
{resources_needed}

Potential Challenges
{potential_challenges}

Documentation & Presentation
Documentation Plan
{documentation_plan}

Presentation Format
{presentation_format}

Feedback and Approval
Teacher-Coach Comments:

Approved Project Plan
• Date:
• Teacher Signature: _____
• Student Signature: _____

This project plan serves as a roadmap for your Personal AI Quest. It may evolve as you progress through your project - that's part of the learning process!"""

            # Store the project plan in session state
            st.session_state.project_plan = project_plan
            st.success("Project plan generated successfully!")
    
    # Display the project plan and download button outside the form
    if 'project_plan' in st.session_state:
        st.subheader("Your Project Plan")
        st.code(st.session_state.project_plan, language="text")
        
        # Add copy button
        st.download_button(
            label="Copy Project Plan",
            data=st.session_state.project_plan,
            file_name="personal_ai_quest_project_plan.txt",
            mime="text/plain"
        )

# Main app logic
def main():
    st.sidebar.title("Navigation")
    if st.sidebar.button("Back to Quiz"):
        st.session_state.current_page = 'quiz'
        st.rerun()
    
    if st.session_state.current_page == 'quiz':
        show_quiz()
    elif st.session_state.current_page == 'results':
        show_results()
    elif st.session_state.current_page == 'project_plan':
        show_project_plan()

if __name__ == "__main__":
    main() 