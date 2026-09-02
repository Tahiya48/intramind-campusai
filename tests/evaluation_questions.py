"""
Evaluation questions for IntraMind CampusAI.

These questions are used to evaluate whether the retriever
returns relevant knowledge-base sources.
"""

EVALUATION_QUESTIONS = [

    # --------------------------------------------------
    # UNIVERSITY INFORMATION
    # --------------------------------------------------

    {
        "question": "What services are available to students?",
        "expected_sources": ["campus_services.md"],
        "category": "University Information",
    },

    {
        "question": "What support is available for academic requirements?",
        "expected_sources": ["academic_support.md"],
        "category": "University Information",
    },

    # --------------------------------------------------
    # MODULE REGISTRATION
    # --------------------------------------------------

    {
        "question": "What should students review before submitting their final registration?",
        "expected_sources": [
            "registration.md",
            "student_handbook.md",
            "policies.md",
            "module_registration_web.md",
        ],
        "category": "Registration",
    },

    {
        "question": "What should students do if they need to add, drop, or withdraw from a module?",
        "expected_sources": ["registration.md"],
        "category": "Registration",
    },

    # --------------------------------------------------
    # INTERNSHIP
    # --------------------------------------------------

    {
        "question": "What documents may students need to submit before starting an internship?",
        "expected_sources": ["internships.md"],
        "category": "Internship",
    },

    {
        "question": "What responsibilities does a workplace supervisor have during an internship?",
        "expected_sources": ["internships.md"],
        "category": "Internship",
    },

    # --------------------------------------------------
    # PDF RETRIEVAL
    # --------------------------------------------------

    {
        "question": "What sections should be included in the internship report according to the Internship Guide?",
        "expected_sources": ["internship_guide.pdf"],
        "category": "PDF Retrieval",
    },

    {
        "question": "What should the executive summary of an internship report describe?",
        "expected_sources": ["internship_guide.pdf"],
        "category": "PDF Retrieval",
    },

    # --------------------------------------------------
    # EXAMINATIONS
    # --------------------------------------------------

    {
        "question": "What should students do if they cannot attend an examination?",
        "expected_sources": [
            "examinations.md",
            "policies.md",
            "attendance.md",
        ],
        "category": "Examinations",
    },

    # --------------------------------------------------
    # WEBSITE
    # --------------------------------------------------

    {
        "question": "Where can students find information about module registration and internships?",
        "expected_sources": ["module_registration_web.md"],
        "category": "Web Retrieval",
    },

    # --------------------------------------------------
    # MULTI-DOCUMENT
    # --------------------------------------------------

    {
        "question": "What should students do before beginning an internship?",
        "expected_sources": ["internships.md"],
        "category": "Multi-Document",
    },

    # --------------------------------------------------
    # UNSUPPORTED QUESTIONS
    # --------------------------------------------------

    {
        "question": "What is Northbridge University's football team called?",
        "expected_sources": [],
        "category": "Unsupported",
    },

    {
        "question": "Who is the president of Northbridge University?",
        "expected_sources": [],
        "category": "Unsupported",
    },

    {
        "question": "What is Northbridge University's official campus population?",
        "expected_sources": [],
        "category": "Unsupported",
    },
]