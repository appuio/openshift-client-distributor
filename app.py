import os
import http.server
import socketserver

PORT = 8080
CLIENT_DIRS = [  # Directories to publish, covering different OpenShift versions
    "/usr/share/atomic-openshift/linux",
    "/usr/share/atomic-openshift/macosx",
    "/usr/share/atomic-openshift/windows",
    "/usr/share/origin/linux",
    "/usr/share/origin/macosx",
    "/usr/share/origin/windows",
    "/tmp/js/cli-download-customization.js"]
TARGET_ROOT = "/tmp/clients"

os.makedirs(TARGET_ROOT, exist_ok=True)
for source_dir in CLIENT_DIRS:
    target_dir = os.path.join(TARGET_ROOT, os.path.basename(source_dir))
    if os.path.exists(source_dir) and not os.path.exists(target_dir):
        os.symlink(source_dir, target_dir)

os.chdir(TARGET_ROOT)

Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()