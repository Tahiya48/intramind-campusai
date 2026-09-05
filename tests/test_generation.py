from src.generation.llm import generate_rag_answer


TEST_CASES = [
    {
        "question": "What services are available to students?",
        "expected_keywords": [
            "Library",
            "IT Support",
            "Academic Support",
        ],
    },
    {
        "question": "What documents may students need to submit before starting an internship?",
        "expected_keywords": [
            "offer letter",
            "internship description",
            "employer information",
        ],
    },
    {
        "question": "What sections should be included in the internship report according to the Internship Guide?",
        "expected_keywords": [
            "Executive Summary",
            "Organization Profile",
            "Conclusion",
        ],
    },
    {
        "question": "Where can students find information about module registration and internships?",
        "expected_keywords": [
            "module registration",
            "internship",
        ],
    },
    {
        "question": "What is Northbridge University's football team called?",
        "expected_keywords": [
            "I could not find the answer",
        ],
    },
]


print("\nINTRAMIND GENERATION EVALUATION")
print("=" * 70)


passed = 0
failed = 0


for index, test_case in enumerate(TEST_CASES, start=1):

    question = test_case["question"]
    expected_keywords = test_case["expected_keywords"]

    result = generate_rag_answer(question)

    answer = result["answer"]
    sources = result["sources"]

    answer_lower = answer.lower()

    keyword_results = [
        keyword.lower() in answer_lower
        for keyword in expected_keywords
    ]

    success = all(keyword_results)

    if success:
        passed += 1
        status = "PASS"
    else:
        failed += 1
        status = "FAIL"

    print(f"\n[{index}/{len(TEST_CASES)}] {question}")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")
    print(f"RESULT: {status}")


print("\n" + "=" * 70)
print("GENERATION EVALUATION SUMMARY")
print("=" * 70)

print(f"Total questions: {len(TEST_CASES)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")

accuracy = (passed / len(TEST_CASES)) * 100

print(f"Generation accuracy: {accuracy:.2f}%")
