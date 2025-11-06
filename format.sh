#!/bin/bash
# Format all Python files with Black and isort

echo "🎨 Formatting Python files..."
black .
isort .
echo "✅ Formatting complete!"
