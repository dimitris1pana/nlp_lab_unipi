from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import language_tool_python
import warnings

warnings.filterwarnings('ignore')

def create_grammar_tree(text):

    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    
    root = Node(f"Text: {text}")
    print(root)
    
    #  sentence node
    sentence_node = Node("Sentence Analysis", parent=root)
    print(sentence_node)
    #  grammar issues node
    if matches:
        issues_node = Node("Grammar Issues", parent=sentence_node)
        for match in matches:
            #  issue node
            issue_node = Node(f"Issue: {match.ruleId}", parent=issues_node)
            Node(f"Message: {match.message}", parent=issue_node)
            Node(f"Context: {match.context}", parent=issue_node)
            suggestions_node = Node("Suggestions", parent=issue_node)
            for suggestion in match.replacements[:3]: 
                Node(suggestion, parent=suggestions_node)
    else:
        Node("No grammar issues found", parent=sentence_node)
    
    print("Grammar Analysis Tree:")
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")
    
    # Export tree as PNG (requires graphviz)
    try:
        DotExporter(root).to_picture("grammar_tree.png")
        print("\nTree visualization saved as 'grammar_tree.png'")
    except Exception as e:
        print("\nCould not create PNG visualization. Make sure graphviz is installed.")




def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    print("Original text:", text)
    print("Corrected text:", corrected_text)
    print("Grammar issues found:", len(matches))
    return matches


