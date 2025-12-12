# Визначаємо корінь проєкту через поточну директорію Makefile
PROJECT_DIR := $(shell pwd)

MIGRATE_BIN := ./bin/migrate
# Використовуємо відносний шлях від кореня проєкту
SOURCE_DIR_RELATIVE := app/db/migrations
SOURCE_URL := file://$(PROJECT_DIR)/$(SOURCE_DIR_RELATIVE)
DB_URL := sqlite3://$(PROJECT_DIR)/expenses.db

migrate-create: 
	$(MIGRATE_BIN) create -ext sql -dir $(SOURCE_DIR_RELATIVE) -seq $(NAME)

migrate-up:
	$(MIGRATE_BIN) -source $(SOURCE_URL) -database $(DB_URL) up

migrate-down:
	$(MIGRATE_BIN) -source $(SOURCE_URL) -database $(DB_URL) down 1

migrate-reset:
	$(MIGRATE_BIN) -source $(SOURCE_URL) -database $(DB_URL) down -all