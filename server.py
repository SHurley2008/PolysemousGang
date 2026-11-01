"""Small local web server that stores registration records in accounts.csv."""

import csv
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parent
ACCOUNTS_FILE = ROOT / "accounts.csv"
FIELDS = [
    "first_name",
    "last_name",
    "age",
    "date_of_birth",
    "province",
    "county",
    "email",
    "address",
]


class SiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self):
        if self.path != "/register":
            self.send_error(404, "Not found")
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400, "Invalid form submission")
            return
        if length <= 0 or length > 16_384:
            self.send_error(400, "Invalid form submission")
            return

        form = parse_qs(self.rfile.read(length).decode("utf-8"), keep_blank_values=True)
        record = {field: form.get(field, [""])[0].strip() for field in FIELDS}
        if any(not value for value in record.values()):
            self.send_error(400, "Please complete every field")
            return
        try:
            age = int(record["age"])
        except ValueError:
            self.send_error(400, "Age must be a number")
            return
        if not 1 <= age <= 120:
            self.send_error(400, "Please enter a valid age")
            return

        needs_header = not ACCOUNTS_FILE.exists() or ACCOUNTS_FILE.stat().st_size == 0
        with ACCOUNTS_FILE.open("a", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
            if needs_header:
                writer.writeheader()
            writer.writerow(record)

        self.send_response(303)
        self.send_header("Location", "/page.html")
        self.send_header("Content-Length", "0")
        self.end_headers()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), SiteHandler)
    print(f"Server listening on port {port}. Open the forwarded port URL (Ctrl+C to stop).")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
