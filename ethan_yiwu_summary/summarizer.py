## summarizer.py
from gensim.summarization import summarize

class Summarizer:
    MIN_TEXT_LENGTH = 60  # Gensim requires a minimum text length to summarize

    def summarize_text(self, text: str, summary_ratio: float = 0.05) -> str:
        """
        Summarize the given text to a specified ratio.

        :param text: The text to summarize.
        :param summary_ratio: The desired ratio of the summary compared to the original text length.
                              The default is set to 5% of the original text.
        :return: The summarized text.
        """
        if not text:
            raise ValueError("Text must be non-empty.")
        if summary_ratio <= 0 or summary_ratio > 1:
            raise ValueError("Summary_ratio must be between 0 and 1.")

        if len(text) < self.MIN_TEXT_LENGTH:
            return text  # Return the original text if it's too short to summarize

        # No need to try-except here as we've already checked the text length
        summary = summarize(text, ratio=summary_ratio)
        return summary

# Example usage:
# summarizer = Summarizer()
# text = "Your long article text goes here..."
# summary = summarizer.summarize_text(text, summary_ratio=0.05)
# print(summary)
