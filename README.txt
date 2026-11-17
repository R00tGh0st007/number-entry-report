REPAIR NUMBER REGISTER

This is a standalone website. It does not read or write Excel.

Run:
  docker compose up -d --build

Open:
  http://localhost:8081

Enter individual numbers such as C123, W1234, D12345.
Any number of digits is accepted after C, D or W.
You can also paste a batch separated by commas, spaces, semicolons or new lines.

The website counts each entry and shows C, D, W and total counts.
Data is stored in the browser's localStorage on that device/browser.
It is not automatically shared between devices or browsers. Export CSV regularly for backup.
To stop:
  docker compose down

If port 8081 is occupied, change "8081:8000" in docker-compose.yml to "8082:8000",
then rebuild and open http://localhost:8082.

ADDED FEATURES
- Search job numbers using the search field.
- Copy WhatsApp report: creates plain text with current filtered totals and job numbers.
- Print text report: opens the browser print dialog with only the plain-text report.
- The report updates when you change the search or prefix filter.

REPORT FORMAT UPDATE
- Friendly date/time.
- C, D and W numbers grouped separately.
- Clear message when there are no entries.
- Technical filter and system footer removed.
