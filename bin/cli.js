const { processMarkdown } = require('../index.js');

const args = process.argv.slice(2);
const [feature, directory, lineNumber, customInput] = args;

if (!feature || !directory) {
	console.log('Usage: article-markdown <feature> <directory> [lineNumber] [customInput]');
	console.log(' feature: 1 (image) or 2 (date)');
	console.log(' directory: Path to folder');
	console.log(' lineNumber: Line number to modify (optional)');
	console.log(' customInput: URL template or date (optional)');
	process.exit(1);
}

processMarkdown(feature, directory, lineNumber, customInput)
	.then(() => console.log('Processing completed.'))
	.catch(err => {
		console.error('Error:', err.message);
		process.exit(1);
	});