# Open SDG - Data starter

This is a starter repository to help in implementing the [Open SDG](https://github.com/open-sdg/open-sdg) platform. [See here for documentation](https://open-sdg.readthedocs.io).



## running the server locally
Make the scripts executable:
```bash
chmod +x serve.py serve.sh
```

Now you can use the development server in these ways:

Using Python script directly:
```bash
python3 serve.py
# Or with custom port:
python3 serve.py --port 3000
```

Using bash script:
```bash
./serve.sh
# Or with custom port:
./serve.sh 3000
```

Build and serve in one go:
```bash
python scripts/build_data.py && python3 serve.py
```

The server will:

Serve files from the _site directory (or whatever directory you specify)
Add proper CORS headers to all responses
Handle OPTIONS preflight requests
Show you the URL to access your site