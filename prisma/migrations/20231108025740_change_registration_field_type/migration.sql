/*
  Warnings:

  - You are about to alter the column `registration` on the `User` table. The data in that column could be lost. The data in that column will be cast from `Int` to `BigInt`.

*/
-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_User" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "registration" BIGINT NOT NULL,
    "picture" TEXT NOT NULL,
    "department" TEXT NOT NULL
);
INSERT INTO "new_User" ("department", "id", "name", "picture", "registration") SELECT "department", "id", "name", "picture", "registration" FROM "User";
DROP TABLE "User";
ALTER TABLE "new_User" RENAME TO "User";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
