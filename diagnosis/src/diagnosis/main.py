import sys
import warnings
from diagnosis.extract import extract_text_from_image,extract_text_from_pdf
from diagnosis.crew import Diagnosis
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")        

def selection():
    try:
        print("1.Image\n2.PDF")
        choice = input("Enter your choice : ").lower()
        if choice == "1" or choice == "image":
            path = input("Enter path to your image : ")
            if path.lower().endswith(".png") or path.lower().endswith(".jpg"):
                content = extract_text_from_image(path)
            else:
                print("Enter a legit path to your image.")
        elif choice == "2" or choice == "pdf":
            path = input("Enter path to your pdf : ")
            if path.lower().endswith(".pdf"):
                content = extract_text_from_pdf(path)
            else:
                print("Enter a legit path to your pdf.")
        else:
            print("select a legit option.(1 or 2).")
            return selection()
        return content
    except Exception as e:
        print("Error occured, try again with legit choice and path.")
        return selection()
    
content = selection()
mid = len(content) // 2
content1, content2 = content[:mid], content[mid:]

def run():
    """
    Run the crew.
    """
    inputs = {
        'content1': f'{content1}',
        'content2': f'{content2}'
    }
    
    try:
        Diagnosis().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'content1': f'{content1}',
        'content2': f'{content2}'
    }
    try:
        Diagnosis().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Diagnosis().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'content1': f'{content1}',
        'content2': f'{content2}'
    }
    
    try:
        Diagnosis().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
