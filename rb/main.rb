require 'google_drive'

if __FILE__ == $0
    session = GoogleDrive::Session.from_service_account_key(ARGV[0])
    spreadsheet = session.spreadsheet_by_title("qotsa")
    worksheet = spreadsheet.worksheets.first
    worksheet.rows.each { |row| puts row.join(" | ") }

    puts "Adding..."
    worksheet[2, 3] = "Guitar and vocals"
    worksheet.insert_rows(worksheet.num_rows + 1, [[6, 'Jon Theodore', 'Drums']])
    worksheet.save
    worksheet.rows.each { |row| puts row.join(" | ") }
    puts "Deleting..."
    worksheet.delete_rows(worksheet.num_rows, 1)
    worksheet[2, 3] = "Guitar"
    worksheet.save
    worksheet.rows.each { |row| puts row.join(" | ") }
end
