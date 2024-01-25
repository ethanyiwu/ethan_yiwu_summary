## web_interface.py
from flask import Flask, request, jsonify
from scraper import Scraper
from summarizer import Summarizer
from cache import Cache
import requests.exceptions

class FlaskApp:
    def __init__(self):
        self.flask_app = Flask(__name__)
        self.scraper = Scraper()
        self.summarizer = Summarizer()
        self.cache = Cache()

        @self.flask_app.route('/summary', methods=['GET'])
        def route_summary():
            # Get URL parameter from request
            url = request.args.get('url', default='', type=str)
            if not url:
                return jsonify({"error": "URL parameter is required."}), 400

            # Get summary_ratio parameter from request or use default
            summary_ratio = request.args.get('summary_ratio', default=0.05, type=float)

            # Check if summary is already cached
            cached_summary = self.cache.get_cached_summary(url)
            if cached_summary:
                return jsonify({"url": url, "summary": cached_summary})

            # If not cached, scrape content and summarize
            try:
                content = self.scraper.get_content(url)
                summary = self.summarizer.summarize_text(content, summary_ratio=summary_ratio)
                # Cache the summary
                self.cache.cache_summary(url, summary)
                return jsonify({"url": url, "summary": summary})
            except requests.exceptions.RequestException as e:
                return jsonify({"error": "Failed to retrieve content: " + str(e)}), 500
            except ValueError as e:
                return jsonify({"error": "Summarization error: " + str(e)}), 500

    def run(self, host='0.0.0.0', port=5000, debug=False):
        """
        Run the Flask application.

        :param host: The hostname to listen on. Defaults to '0.0.0.0' to make the server publicly available.
        :param port: The port of the webserver. Defaults to 5000.
        :param debug: Whether to run the server in debug mode. Defaults to False.
        """
        self.flask_app.run(host=host, port=port, debug=debug)

# If this script is run directly, create an instance of FlaskApp and call run
if __name__ == '__main__':
    app = FlaskApp()
    app.run()
