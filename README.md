# Ai-Contract-Assistant
An AI Assistant that extracts content from Business contracts and provides Key points, segregates the content into Clauses and Sub clauses and when provided with a template shows deviations.

## Documentation

[*Docs*](https://github.com/Ashuradhipathi/Ai-Contract-Assistant/blob/main/Documentation.md)

## Set up

```
pip install -r requirements.txt
```
### Run

```
streamlit run New_Contract.py
```

# Contribution Guidelines

Thank you for considering contributing to this project! To ensure smooth collaboration, please follow these guidelines when making changes or adding new features.

## General Guidelines
- **Consistency**: Maintain consistency with the existing code structure, documentation format, and naming conventions.
- **Testing**: Thoroughly test any new feature or fix before submitting. Ensure that existing features are not affected.
- **Documentation**: Update relevant sections in the documentation when adding or modifying functionality, including utility functions, dependencies, or UI pages.

## Submitting Contributions
1. **Fork the repository** and create a new branch for your feature or fix.
2. **Make your changes**. Ensure they adhere to the guidelines listed below.
3. **Test your changes**. If applicable, write tests to validate the new functionality.
4. **Submit a Pull Request (PR)**. Make sure to clearly describe the changes, purpose, and any dependencies.

## Dependency Management
- Ensure that all dependencies are up-to-date and compatible with existing ones.
- If you introduce a new dependency, update the `# Dependencies` section in the documentation accordingly, including links to its documentation.

## Adding New Utility Functions
- When adding new utility functions, ensure they follow the same structure and naming conventions used in `rag.py` and `utils.py`.
- Place any utility functions related to extracting text, key points, clauses, or deviations in `utils.py`.
- Clearly document the purpose and usage of any new functions in the relevant section of the code and in the `# Utility functions` section of the documentation.

## Pages Folder Structure
- **Home Page**: If you modify `New_contract.py`, ensure that it still handles file uploads and integrates with existing helper functions for text extraction and vector store updates.
- **Additional Pages**: All new pages must be added to the `Pages` folder. If the page involves querying the contract or template, ensure it correctly uses helper functions.
- **UI Components**: Any new page should follow the structure of existing ones like `Clauses`, `Key Points`, and `Deviations`. Use appropriate helper functions (`extract_clauses`, `extract_keypoints`, `find_deviations`) for their respective functionality.

### Page-Specific Guidelines
- **Clauses**: New components should use the `extract_clauses` function.
- **Key Points**: Ensure the UI integrates with the `extract_keypoints` function.
- **Deviations**: Use the `find_deviations` function to maintain consistency with other pages.

## Code Style
- Follow Python best practices and the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Keep functions modular and concise.
- Write clear and descriptive docstrings for all functions.

## Testing
- Before submitting a PR, ensure that all code is tested.
- If applicable, create new test cases to cover the new features or bug fixes.
- Validate that existing functionality is not broken by running the full test suite.

## Pull Request Requirements
- A descriptive title and summary of the changes.
- Reference any related issues or tasks in the PR description.
- Include a section on **Testing** explaining how you tested the new functionality.
- Ensure that the CI pipeline (if any) passes before submitting the PR for review.

---

By following these guidelines, you help maintain the quality and integrity of the project. Happy coding!
