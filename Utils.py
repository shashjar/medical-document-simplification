from rouge_score import rouge_scorer
from readability import Readability


def rouge_score(reference : str, generated : str, score_type : any) -> dict:
    """
    Generates Rouge Score for two given summaries

    Args:
        reference (str): Reference summary
        generated (str): Generated summary
        score_type (any): Number 1-9 or "L"

    Returns:
        dict: Rouge Score type with precision, recall, and fmeasure
        Ex: {'rougeL': Score(precision=0.8571428571428571, recall=1.0, fmeasure=0.923076923076923)}
    """
    scorer = rouge_scorer.RougeScorer(['rouge' + str(score_type)], use_stemmer=True)
    return scorer.score(reference, generated)
        
def flesch_kincaid(generated : str) -> float:
    """
    Generates Flesch-Kincaid score for a given summary
    (100 word min)

    Args:
        generated (str): Generated Summary

    Returns:
        float: Flesch-Kincaid score - estimated grade level of reading difficulty
    """
    r = Readability(generated)
    fk = r.flesch_kincaid()
    return fk.score

def linsear_write(generated : str) -> float:
    """
    Generates Linsear Write score for a given summary
    (100 word min)

    Args:
        generated (str): Generated Summary

    Returns:
        float: Linsear Write score - readability metric
    """
    r = Readability(generated)
    lw = r.linsear_write()
    return lw.score