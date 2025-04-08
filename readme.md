# Article Markdown
A Node.js library to process markdown files using Python.

## Installation
npm install article-markdown

## Usage
const { processMarkdown } = require('article-markdown');
// Thay đổi hình ảnh
processMarkdown('1', './path/to/folder', '5', 'https://example.com/image-{number}.jpg');
// Thay đổi ngày tháng
processMarkdown('2', './path/to/folder', '2', '2025-04-01');