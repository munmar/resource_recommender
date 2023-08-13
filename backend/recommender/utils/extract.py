import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

technical_skills = {
  'languages': ['HTML/CSS', 'Python', 'SQL', 'TypeScript', 'Bash/Shell (all shells)', 'Java', 'C#', 'C++', 'C', 'PHP', 'PowerShell', 'Go', 'Rust', 'Kotlin', 'Ruby', 'Lua', 'Dart', 'Assembly', 'Swift', 'R', 'Visual Basic (.Net)', 'MATLAB', 'VBA', 'Groovy', 'Delphi', 'Scala', 'Perl', 'Elixir', 'Objective-C', 'Haskell', 'GDScript', 'Lisp', 'Solidity', 'Clojure', 'Julia', 'Erlang', 'F#', 'Fortran', 'Prolog', 'Zig', 'Ada', 'OCaml', 'Apex', 'Cobol', 'SAS', 'Crystal', 'Nim', 'APL', 'Flow', 'Raku'], 
  'databases': ['MySQL', 'SQLite', 'MongoDB', 'Microsoft SQL Server', 'Redis', 'MariaDB', 'Elasticsearch', 'Oracle', 'Dynamodb', 'Firebase Realtime Database', 'Cloud Firestore', 'BigQuery', 'Microsoft Access', 'H2', 'Cosmos DB', 'Supabase', 'InfluxDB', 'Cassandra', 'Snowflake', 'Neo4J', 'IBM DB2', 'Solr', 'Firebird', 'Couch DB', 'Clickhouse', 'Cockroachdb', 'Couchbase', 'DuckDB', 'Datomic', 'RavenDB', 'TiDB'], 
  'cloud platforms': ['Microsoft Azure', 'Google Cloud', 'Firebase', 'Cloudflare', 'Digital Ocean', 'Heroku', 'Vercel', 'Netlify', 'VMware', 'Hetzner', 'Linode, now Akamai', 'Managed Hosting', 'OVH', 'Oracle Cloud Infrastructure (OCI)', 'OpenShift', 'Fly.io', 'Vultr', 'Render', 'OpenStack', 'IBM Cloud Or Watson', 'Scaleway', 'Colocation'], 
  'web frameworks': ['React', 'jQuery', 'Express', 'Angular', 'Next.js', 'ASP.NET CORE', 'Vue.js', 'WordPress', 'ASP.NET', 'Flask', 'Spring Boot', 'Django', 'Laravel', 'FastAPI', 'AngularJS', 'Svelte', 'Ruby on Rails', 'NestJS', 'Blazor', 'Nuxt.js', 'Symfony', 'Deno', 'Gatsby', 'Fastify', 'Phoenix', 'Drupal', 'CodeIgniter', 'Solid.js', 'Remix', 'Elm', 'Play Framework', 'Lit', 'Qwik'], 
  'other frameworks and libraries': ['NumPy', 'Pandas', '.NET Framework (1.0 - 4.8)', 'Spring Framework', 'RabbitMQ', 'TensorFlow', 'Scikit-Learn', 'Flutter', 'Apache Kafka', 'Torch/PyTorch', 'React Native', 'Opencv', 'Electron', 'OpenGL', 'Qt', 'CUDA', 'Keras', 'Apache Spark', 'SwiftUI', 'Xamarin', 'Ionic', 'Hugging Face Transformers', 'GTK', 'Cordova', '.NET MAUI', 'Hadoop', 'Tauri', 'Capacitor', 'Tidyverse', 'Quarkus', 'Ktor', 'MFC', 'JAX', 'Micronaut', 'Uno Platform'], 
  'tools': ['npm', 'Pip', 'Homebrew', 'Yarn', 'Webpack', 'Make', 'Kubernetes', 'NuGet', 'Maven (build tool)', 'Gradle', 'Vite', 'Visual Studio Solution', 'CMake', 'Cargo', 'GNU GCC', 'Terraform', 'MSBuild', 'Ansible', 'Chocolatey', 'Composer', "LLVM's Clang", 'APT', 'Unity 3D', 'Pacman', 'pnpm', 'MSVC', 'Podman', 'Ninja', 'Unreal Engine', 'Godot', 'Ant', 'Google Test', 'Nix', 'Meson', 'QMake', 'Puppet', 'Dagger', 'Chef', 'Catch2', 'Pulumi', 'Bun', 'Wasmer', 'doctest', 'SCons', 'bandit', 'cppunit', 'Boost.Test', 'build2', 'tunit', 'lest', 'snitch', 'CUTE', 'ELFspy', 'liblittletest'], 
  'ide': ['Visual Studio', 'IntelliJ IDEA', 'Notepad++', 'Vim', 'Android Studio', 'PyCharm', 'Jupyter Notebook/JupyterLab', 'Sublime Text', 'Neovim', 'Eclipse', 'Xcode', 'Nano', 'WebStorm', 'PhpStorm', 'Atom', 'Rider', 'DataGrip', 'CLion', 'IPython', 'Emacs', 'VSCodium', 'Goland', 'Netbeans', 'RStudio', 'Code::Blocks', 'Qt Creator', 'Rad Studio (Delphi, C++ Builder)', 'Fleet', 'Helix', 'Kate', 'Spyder', 'RubyMine', 'Geany', 'BBEdit', 'TextMate', 'Micro', 'Nova', 'condo'], 
  'async tools': ['Confluence', 'Markdown File', 'Trello', 'Notion', 'GitHub Discussions', 'Azure Devops', 'Miro', 'Wikis', 'Asana', 'Clickup', 'Doxygen', 'Redmine', 'Monday.com', 'Stack Overflow for Teams', 'YouTrack', 'Microsoft Planner', 'Airtable', 'Linear', 'Basecamp', 'Microsoft Lists', 'Smartsheet', 'Shortcut', 'Wrike', 'Adobe Workfront', 'Redocly', 'Document360', 'Nuclino', 'Swit', 'Dingtalk (Teambition)', 'Tettra', 'Workzone', 'Planview Projectplace Or Clarizen', 'Wimi', 'Cerri', 'Leankor'], 
  'sync tools': ['Slack', 'Zoom', 'Discord', 'Google Meet', 'Whatsapp', 'Telegram', 'Skype', 'Signal', 'Google Chat', 'Cisco Webex Teams', 'Mattermost', 'Jitsi', 'Matrix', 'IRC', 'Rocketchat', 'Zulip', 'Ringcentral', 'Symphony', 'Wire', 'Wickr', 'Unify Circuit', 'Coolfire Core']
}

def extract_technical_skills(description):
  tokens = word_tokenize(description)
  pos_tags = pos_tag(tokens)

  technical_skills = []
  for word, tag in pos_tags:
    if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
      technical_skills.append(word)

  return technical_skills

# Function to check if any skill is present in the description
def contains_skill(description):
  for category, skills in technical_skills.items():
    for skill in skills:
      # Construct a regular expression pattern to match whole words
      pattern = r'\b' + re.escape(skill.lower()) + r'\b'
      if re.search(pattern, description.lower()):
        return True
  return False
