const { _: [sqlFileName], e = "local", env = e } = require("simple-argv")

console.log(`Eseguo ${sqlFileName}.sql in ambiente ${env}`)

const mysql = require("mysql")
const config = require(`./db-config.json`)
const { readFileSync } = require("fs")
const { join } = require("path")
const pool = require("./pool.js")
const sql = readFileSync(join(__dirname, `${sqlFileName}`), "utf8")


pool.query(sql,(err, data) => {
  if (err) {
    console.log(err)
  } else {
    console.log(data)
  }
})