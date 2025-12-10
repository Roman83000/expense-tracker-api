MIGRATE_BIN := ./bin/migrate
SOURCE_DIR := file:///Users/roman/workspace/expense_api/app/db/migrations
DB_URL := sqlite3:///Users/roman/workspace/expense_api/expenses.db

#all: $(MIGRATE_BIN) $(SOURCE_DIR) $(DB_URL)

migrate-create: 
	$(MIGRATE_BIN) create -ext sql -dir /Users/roman/workspace/expense_api/app/db/migrations -seq add_new_table
migrate-up:
	$(MIGRATE_BIN) -source $(SOURCE_DIR) -database $(DB_URL) up

migrate-down:
	$(MIGRATE_BIN) -source $(SOURCE_DIR) -database $(DB_URL) down 1

migrate-reset:
	$(MIGRATE_BIN) -source $(SOURCE_DIR) -database $(DB_URL) down -all