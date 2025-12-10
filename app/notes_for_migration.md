#Змінні для команд (запускати з папки, де знаходиться ./migrate):
# MIGRATE_BIN=./migrate
# SOURCE_DIR=file:///Users/roman/workspace/expense_api/app/db/migrations
# DB_URL= sqlite:///Users/roman/workspace/expense_api/app/expenses.db
#
# 1. СТВОРИТИ НОВІ ФАЙЛИ МІГРАЦІЇ:
#    ./migrate create -ext sql -dir /Users/roman/workspace/expense_api/app/db/migrations -seq add_new_table
#
# 2. ЗАСТОСУВАТИ ВСІ МІГРАЦІЇ (КРОК ВПЕРЕД):
#    $MIGRATE_BIN -source $SOURCE_DIR -database $DB_URL up
#
# 3. ВІДКОТИТИ ОСТАННЮ МІГРАЦІЮ (КРОК НАЗАД):
#    $MIGRATE_BIN -source $SOURCE_DIR -database $DB_URL down 1
#
# 4. ВІДКОТИТИ ВСІ МІГРАЦІЇ (ОЧИЩЕННЯ):
#    $MIGRATE_BIN -source $SOURCE_DIR -database $DB_URL down -all
#
# 5. ПОКАЗАТИ ПОТОЧНУ ВЕРСІЮ:
#    $MIGRATE_BIN -source $SOURCE_DIR -database $DB_URL version
#