from src.retrieval.retriever import retrieve_relevant_chunks
from tests.evaluation_questions import EVALUATION_QUESTIONS


def run_evaluation():

    print("\n")
    print("=" * 70)
    print("INTRAMIND RETRIEVAL EVALUATION")
    print("=" * 70)

    total_questions = len(EVALUATION_QUESTIONS)
    passed_questions = 0

    for index, item in enumerate(
        EVALUATION_QUESTIONS,
        start=1,
    ):

        question = item["question"]
        expected_sources = item["expected_sources"]
        category = item["category"]

        results = retrieve_relevant_chunks(
            query=question,
            n_results=10,
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        retrieved_sources = []

        for metadata in metadatas:

            source = metadata.get("source")

            if source and source not in retrieved_sources:

                retrieved_sources.append(source)

        # --------------------------------------------------
        # EVALUATE RESULT
        # --------------------------------------------------

        if not expected_sources:

            # Unsupported question should not retrieve sufficiently relevant information.
            passed = len(documents) == 0

        else:

            # At least one expected source should be retrieved.
            passed = any(
                source in retrieved_sources
                for source in expected_sources
            )

        # --------------------------------------------------
        # DISPLAY RESULT
        # --------------------------------------------------

        print()
        print(f"[{index}/{total_questions}] {question}")
        print(f"Category: {category}")

        print(
            f"Expected source(s): "
            f"{expected_sources if expected_sources else 'None'}"
        )

        print(
            f"Retrieved source(s): "
            f"{retrieved_sources if retrieved_sources else 'None'}"
        )

        if distances:

            print(
                f"Best distance: {min(distances):.4f}"
            )

        if passed:

            print("RESULT: PASS")

            passed_questions += 1

        else:

            print("RESULT: FAIL")

    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------

    failed_questions = (
        total_questions - passed_questions
    )

    accuracy = (
        passed_questions / total_questions * 100
        if total_questions
        else 0
    )

    print()
    print("=" * 70)
    print("EVALUATION SUMMARY")
    print("=" * 70)

    print(
        f"Total questions: {total_questions}"
    )

    print(
        f"Passed: {passed_questions}"
    )

    print(
        f"Failed: {failed_questions}"
    )

    print(
        f"Retrieval accuracy: {accuracy:.2f}%"
    )

    print("=" * 70)


if __name__ == "__main__":
    run_evaluation()