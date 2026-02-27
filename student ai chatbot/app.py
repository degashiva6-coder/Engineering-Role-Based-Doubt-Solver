from flask import Flask, render_template, request

app = Flask(__name__)

# Branch -> subjects mapping
BRANCH_SUBJECTS = {
    "Computer Science": [
        "Data Structures", 
        "Operating Systems", 
        "Algorithms", 
        "Computer Networks",
        "Database Management Systems",
        "Web Development",
        "Artificial Intelligence",
        "Software Engineering",
        "Compiler Design",
        "Discrete Mathematics"
    ]
}

# Example doubts for subject quick-fill
SAMPLE_DOUBTS = {
    "Data Structures": [
        "How does a binary search tree work?",
        "When should I use a hash table vs array?",
        "Explain tree traversal methods",
        "What is the difference between stack and queue?",
        "How does a linked list work?",
        "What are heaps and priority queues?"
    ],
    "Operating Systems": [
        "What is context switching?",
        "How do semaphores prevent race conditions?",
        "Explain virtual memory briefly",
        "What is a process vs thread?",
        "How does page replacement work?",
        "What is inter-process communication?"
    ],
    "Algorithms": [
        "What's the difference between merge sort and quick sort?",
        "Explain dynamic programming with an example",
        "When to use greedy algorithms?",
        "What is binary search and how is it different from linear search?",
        "Explain the divide and conquer approach",
        "What is backtracking with examples?"
    ],
    "Computer Networks": [
        "What is the difference between TCP and UDP?",
        "How does routing work at a high level?",
        "What does HTTP do?",
        "Explain the OSI model layers",
        "What is IP and how does IP addressing work?",
        "What is DNS and how does it work?"
    ],
    "Database Management Systems": [
        "What are ACID properties and why are they important?",
        "Explain normalization and its forms",
        "What is the difference between SQL and NoSQL?",
        "What is a primary key and foreign key?",
        "Explain joins in database queries",
        "What is indexing and why is it important?"
    ],
    "Web Development": [
        "What is the difference between frontend and backend?",
        "Explain REST API principles",
        "How does HTTP request-response work?",
        "What are cookies and sessions?",
        "Explain MVC architecture",
        "What is CORS and why is it important?"
    ],
    "Artificial Intelligence": [
        "What is machine learning and its types?",
        "Explain supervised vs unsupervised learning",
        "What is neural network and deep learning?",
        "What is overfitting and underfitting?",
        "Explain cluster analysis in machine learning",
        "What are activation functions in neural networks?"
    ],
    "Software Engineering": [
        "What are SDLC models and their phases?",
        "Explain design patterns with examples",
        "What is agile methodology?",
        "What is version control and why is it important?",
        "Explain unit testing and test-driven development",
        "What is CI/CD pipeline?"
    ],
    "Compiler Design": [
        "Explain lexical analysis and tokenization",
        "What is the role of parser in compilation?",
        "What is code generation?",
        "What is semantic analysis in compilation?",
        "Explain the symbol table in compilers",
        "What is intermediate representation?"
    ],
    "Discrete Mathematics": [
        "What are sets and set operations?",
        "Explain graph theory basics",
        "What is combinatorics and probability?",
        "What are boolean algebra and logic gates?",
        "Explain trees in discrete mathematics",
        "What is mathematical induction?"
    ]
}


def make_list(items):
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def get_response(branch: str, subject: str, doubt: str) -> str:
    """Produce an HTML explanation based on the provided branch, subject and free‑text doubt.

    This function uses simple rule-based logic (no external calls or databases).
    Keywords inside the student's doubt help choose which subtopic to elaborate; otherwise
    a standard description for the subject is returned. The output is a string containing
    HTML so it can be safely rendered using ``{{ response|safe }}`` in the template.
    """

    d = (doubt or "").strip()
    dl = d.lower()

    # echo the question for clarity
    intro = (
        f"<p class=\"response-question\"><strong>Q:</strong> {d}</p>"
        f"<p class=\"response-intro\">Hi there! As your friendly engineering professor, here is a clear, concise explanation "
        f"for your doubt about <strong>{subject}</strong> in <strong>{branch}</strong>.</p>"
    )

    # default values
    definition = "This topic covers fundamental ideas that engineers encounter in their courses and work."
    examples = [
        "A general engineering example illustrating the idea.",
        "Another applied scenario where this concept appears."
    ]
    industry = "Core engineering disciplines apply these principles across multiple industries."
    keywords_list = ["core", "fundamental"]
    summary = "This explanation should give you a grasp of the underlying concept so you can explore further."

    if branch == "Computer Science":
        if subject == "Algorithms":
            definition = (
                "Algorithms are step-by-step procedures to solve computational problems with measurable resources."
            )
            if any(k in dl for k in ["sort", "merge", "quick", "complexity"]):
                examples = [
                    "Sorting large datasets for database indexing.",
                    "Choosing the right sort for memory-limited devices."
                ]
                keywords_list = ["time complexity", "space complexity", "divide and conquer", "greedy"]
                industry = "Search engines, data processing, and performance-critical software rely on algorithmic choices."
                summary = "Pick algorithms by correctness and complexity; test on realistic inputs."
            elif any(k in dl for k in ["dynamic", "dp", "memo"]):
                examples = [
                    "Sequence alignment in bioinformatics using dynamic programming.",
                    "Optimizing resource allocation in software using memoization."
                ]
                keywords_list = ["dynamic programming", "overlapping subproblems", "optimal substructure"]
                industry = "Optimization tasks in finance, logistics, and machine systems often use DP techniques."
                summary = "Dynamic programming transforms exponential solutions into efficient ones by reusing results."
            elif any(k in dl for k in ["binary", "search", "linear"]):
                examples = [
                    "Finding a contact in a sorted phone book using binary search.",
                    "Server load balancing selecting best resource using binary search.",
                    "Linear search through a to-do list to find an item."
                ]
                keywords_list = ["binary search", "O(log n)", "sorted", "divide and conquer"]
                industry = "Database indexes and search engines rely on binary search for fast lookups."
                summary = "Binary search is exponentially faster than linear on sorted data."
            elif any(k in dl for k in ["divide", "conquer", "merge", "recursive"]):
                examples = [
                    "Merge sort divides arrays, conquers each half, then merges results.",
                    "File system traversal recursively explores directory trees."
                ]
                keywords_list = ["divide and conquer", "recursion", "subproblem", "combine"]
                industry = "Parallel processing, big data, and system algorithms use divide-and-conquer."
                summary = "Divide-and-conquer breaks hard problems into simpler identical subproblems."
            elif any(k in dl for k in ["backtrack", "explore", "constraint", "pruning"]):
                examples = [
                    "N-Queens problem explores placements and backtracks on conflicts.",
                    "Sudoku solvers try number placements and undo invalid ones."
                ]
                keywords_list = ["backtracking", "constraint satisfaction", "pruning", "search tree"]
                industry = "Constraint solvers, game AI, and combinatorial optimization use backtracking."
                summary = "Backtracking systematically explores choices and undoes failed attempts."
            else:
                examples = [
                    "Greedy algorithms selecting locally best options for global problems.",
                    "Graph algorithms finding connected components or shortest paths."
                ]
                keywords_list = ["algorithm", "optimization", "efficiency", "correctness"]
                industry = "Every software system relies on choosing the right algorithm for the task."
        elif subject == "Computer Networks":
            definition = (
                "Computer Networks enable systems to exchange data using protocols, addressing, and routing."
            )
            if any(k in dl for k in ["tcp", "udp", "http"]):
                examples = [
                    "Streaming video uses UDP for low-latency delivery.",
                    "Web browsing relies on TCP and HTTP for reliable transfers."
                ]
                keywords_list = ["protocol", "packet", "router", "latency", "throughput"]
                industry = "Cloud services, telecom, and distributed systems depend on robust networking."
                summary = "Protocols and layering abstract network complexity and ensure reliable communication."
            elif any(k in dl for k in ["osi", "layer", "model", "architecture"]):
                examples = [
                    "HTTP operates at Layer 7; IP at Layer 3; Ethernet at Layer 2.",
                    "Firewalls inspect packets at different OSI layers for security."
                ]
                keywords_list = ["OSI model", "seven layers", "physical", "network", "application"]
                industry = "Network engineers use the OSI model to troubleshoot and design systems."
                summary = "OSI model abstracts networking into 7 layers; each has protocols and functions."
            elif any(k in dl for k in ["dns", "domain", "name resolution", "lookup"]):
                examples = [
                    "Typing google.com triggers DNS to resolve it to an IP address.",
                    "DNS caching at ISPs speeds up repeated lookups."
                ]
                keywords_list = ["DNS", "domain name", "resolution", "record", "nameserver"]
                industry = "DNS is critical infrastructure; performance and security are paramount."
                summary = "DNS translates human-readable names to IP addresses via hierarchical lookup."
            elif any(k in dl for k in ["ip", "address", "ipv4", "ipv6", "routing"]):
                examples = [
                    "IP routing tables guide packets to correct networks.",
                    "IPv6 addresses provide far more address space than IPv4."
                ]
                keywords_list = ["IP address", "routing", "subnet", "gateway", "CIDR"]
                industry = "ISPs and data centers carefully manage IP allocation and routing."
                summary = "IP addresses identify devices; routing tables guide traffic to destinations."
            else:
                examples = [
                    "Network protocols standardizing communication between devices.",
                    "Routers and switches forwarding data based on addresses."
                ]
                keywords_list = ["network", "communication", "protocol", "routing"]
                industry = "Networking is the backbone of the digital world."

        elif subject == "Data Structures":
            definition = (
                "Data Structures are organized ways to store and manage data so algorithms can access and "
                "modify it efficiently."
            )
            if any(k in dl for k in ["tree", "binary", "bst", "trie"]):
                examples = [
                    "Routing tables in networks often use tree-like structures for prefix matching.",
                    "File system directories are represented as trees for hierarchical organization."
                ]
                keywords_list = ["tree", "node", "root", "leaf", "traversal"]
                industry = (
                    "Search engines, databases, and compilers use tree structures for parsing, indexing, and fast lookups."
                )
                summary = "Trees organize hierarchical data; traverse and balance them for performance."
            elif any(k in dl for k in ["hash", "hash table", "hash map"]):
                examples = [
                    "Caching DNS lookups using hash tables for O(1) average retrieval.",
                    "Python dictionaries internally use hash tables for fast lookups."
                ]
                keywords_list = ["hash function", "collision", "load factor", "hash table", "dictionary"]
                industry = "Databases, caching layers, and indexing engines rely heavily on hash tables."
                summary = "Hash tables provide fast average-case lookups; handle collisions carefully."
            elif any(k in dl for k in ["graph", "dfs", "bfs", "shortest"]):
                examples = [
                    "Road and traffic networks model intersections as graph nodes and roads as edges.",
                    "Social networks model users and their relationships using graphs."
                ]
                keywords_list = ["graph", "vertex", "edge", "path", "connectivity"]
                industry = "Transportation planning, recommendation systems, and network analysis rely on graphs."
                summary = "Graphs model pairwise relationships; use traversals and algorithms to extract insights."
            elif any(k in dl for k in ["stack", "queue", "difference"]):
                examples = [
                    "Browser back button uses a stack to track visited pages.",
                    "CPU scheduling uses queues to manage ready processes."
                ]
                keywords_list = ["LIFO", "FIFO", "push", "pop", "enqueue", "dequeue"]
                industry = "Operating systems and memory management heavily use stacks and queues."
                summary = "Stack is LIFO; queue is FIFO. Choose based on needed access pattern."
            elif any(k in dl for k in ["linked", "link", "pointer"]):
                examples = [
                    "Undo/redo functionality in editors uses doubly linked lists.",
                    "LRU cache eviction uses doubly linked lists for efficient memory management."
                ]
                keywords_list = ["node", "pointer", "singly linked", "doubly linked", "circular"]
                industry = "Memory management and dynamic data manipulation use linked lists extensively."
                summary = "Linked lists excel at insertion/deletion; arrays at random access trade-offs exist."
            elif any(k in dl for k in ["heap", "priority"]):
                examples = [
                    "Priority queues in OS schedulers use heaps to select next process.",
                    "Dijkstra's algorithm uses min-heaps to find shortest paths efficiently."
                ]
                keywords_list = ["heap", "priority queue", "min-heap", "max-heap", "heapify"]
                industry = "Real-time systems and game engines use heaps for efficient priority management."
                summary = "Heaps maintain priority efficiently; use for top-k queries and scheduling."
            else:
                examples = [
                    "Using arrays to store sensor readings in embedded systems.",
                    "Hash tables powering fast lookups in caches and key-value stores."
                ]
                keywords_list = ["array", "list", "stack", "queue", "hash table"]
                industry = "Databases, caching, and system internals depend on efficient data structures."

        elif subject == "Operating Systems":
            definition = (
                "An Operating System (OS) manages hardware and software resources, providing services to programs "
                "and users."
            )
            if any(k in dl for k in ["process", "context", "scheduling"]):
                examples = [
                    "A scheduler deciding which program gets CPU time on a multicore system.",
                    "Process isolation that prevents one program from corrupting another's memory."
                ]
                keywords_list = ["process", "thread", "scheduling", "context switch"]
                industry = "Cloud providers and OS vendors optimize scheduling for fairness and throughput."
                summary = "OS components like schedulers and memory managers ensure programs run efficiently and safely."
            elif any(k in dl for k in ["thread", "process vs", "difference"]):
                examples = [
                    "Web server uses multiple threads to handle concurrent client requests.",
                    "Python's multiprocessing uses separate processes to bypass the Global Interpreter Lock."
                ]
                keywords_list = ["thread", "process", "lightweight", "shared memory", "concurrency"]
                industry = "Concurrent applications choose threads or processes based on performance and isolation needs."
                summary = "Threads share memory and are lightweight; processes are isolated and heavyweight."
            elif any(k in dl for k in ["page", "replacement", "virtual"]):
                examples = [
                    "LRU page replacement evicts least-recently-used pages to manage memory.",
                    "OS swaps pages to disk when physical memory fills up."
                ]
                keywords_list = ["page replacement", "virtual memory", "paging", "TLB", "page fault"]
                industry = "Memory management is critical for OS efficiency, especially on embedded systems."
                summary = "Paging enables abstract memory; replacement policies balance speed and space."
            elif any(k in dl for k in ["ipc", "inter-process", "communication"]):
                examples = [
                    "Pipes in Unix shells pass data between processes.",
                    "Message queues in microservices decouple service communication."
                ]
                keywords_list = ["IPC", "pipes", "sockets", "message queues", "shared memory"]
                industry = "Distributed systems and microservices rely on robust inter-process communication."
                summary = "IPC methods trade-off latency, simplicity, and flexibility based on needs."
            elif any(k in dl for k in ["deadlock", "mutex", "semaphore"]):
                examples = [
                    "Two processes waiting on each other for locks (classic deadlock).",
                    "Using semaphores to coordinate access to a limited pool of resources."
                ]
                keywords_list = ["deadlock", "resource allocation", "locking", "synchronization"]
                industry = "Real-time systems and databases handle synchronization carefully to avoid deadlocks."
                summary = "Avoid circular waits, use ordering or timeouts, and design for safe concurrent access."
            else:
                examples = [
                    "Virtual memory enabling programs to use more memory than physically available.",
                    "Device drivers letting OS interact with printers and network cards."
                ]
                keywords_list = ["virtual memory", "paging", "drivers", "kernel"]
                industry = "System software, embedded devices, and cloud platforms rely on core OS services."

        elif subject == "Database Management Systems":
            definition = (
                "Database Management Systems (DBMS) are software tools for storing, managing, and querying data efficiently."
            )
            if any(k in dl for k in ["acid", "acid properties"]):
                examples = [
                    "Banking systems use ACID to ensure money transfers are reliable.",
                    "E-commerce platforms apply ACID to handle concurrent orders safely."
                ]
                keywords_list = ["atomicity", "consistency", "isolation", "durability"]
                industry = "Financial institutions and mission-critical systems rely on ACID compliance."
                summary = "ACID ensures reliable transactions; each part is crucial for data integrity."
            elif any(k in dl for k in ["normalization", "normal form", "1nf", "2nf", "3nf"]):
                examples = [
                    "Organizing student data into separate tables for courses and records.",
                    "Designing a library database without data redundancy."
                ]
                keywords_list = ["normalization", "decomposition", "functional dependency", "normal forms"]
                industry = "Database designers use normalization to minimize storage and improve query efficiency."
                summary = "Normalization eliminates redundancy and improves data quality."
            elif any(k in dl for k in ["primary", "key", "unique", "constraint"]):
                examples = [
                    "Student ID is a primary key uniquely identifying each student record.",
                    "Email addresses are often unique constraints in user tables."
                ]
                keywords_list = ["primary key", "foreign key", "unique constraint", "data integrity"]
                industry = "Database schemas use primary keys to enforce data integrity and enable fast lookups."
                summary = "Primary keys uniquely identify records; foreign keys link related tables."
            elif any(k in dl for k in ["join", "inner", "left", "right", "outer"]):
                examples = [
                    "Joining students and courses tables to find which courses each student takes.",
                    "LEFT JOIN to list all students and their enrollments if any."
                ]
                keywords_list = ["join", "inner join", "left join", "right join", "cross product"]
                industry = "Complex queries in data analysis and reporting heavily rely on joins."
                summary = "Joins combine data from multiple tables based on relationships."
            elif any(k in dl for k in ["index", "indexing", "performance", "search"]):
                examples = [
                    "B-tree indexes on student IDs speed up lookups from seconds to milliseconds.",
                    "Full-text indexes enable fast searching in large document collections."
                ]
                keywords_list = ["index", "B-tree", "search", "query optimization", "trade-off"]
                industry = "Indexes are crucial for database performance; they must be carefully chosen."
                summary = "Indexes speed up retrieval at the cost of slower insertions and updates."
            elif any(k in dl for k in ["sql", "nosql"]):
                examples = [
                    "SQL for structured data like financial records; NoSQL for flexible documents.",
                    "Choosing MongoDB for rapid development vs PostgreSQL for strict schemas."
                ]
                keywords_list = ["relational", "document", "scalability", "schema"]
                industry = "Startups prefer NoSQL flexibility; enterprises often use SQL for consistency."
                summary = "SQL excels at structured data; NoSQL at scalability and flexibility."
            else:
                examples = [
                    "Designing schemas to minimize redundancy and extraction.",
                    "Querying databases to extract insights from large datasets."
                ]
                keywords_list = ["database", "schema", "query", "efficiency"]
                industry = "Every application that stores data relies on a well-designed database."

        elif subject == "Web Development":
            definition = (
                "Web Development involves building applications that run in browsers and web servers using HTML, CSS, JavaScript, and backend frameworks."
            )
            if any(k in dl for k in ["frontend", "backend"]):
                examples = [
                    "Frontend handles UI and user interactions; backend processes and stores data.",
                    "React for frontend, Node.js for backend in a full-stack application."
                ]
                keywords_list = ["frontend", "backend", "client-server", "full-stack"]
                industry = "Web applications power e-commerce, social media, and SaaS platforms."
                summary = "Frontend is what users see; backend is the logic that powers it."
            elif any(k in dl for k in ["rest", "api", "restful"]):
                examples = [
                    "Twitter API exposes endpoints for tweets, users, and timelines.",
                    "Google Maps API provides location services to third-party apps."
                ]
                keywords_list = ["REST", "endpoints", "HTTP methods", "stateless"]
                industry = "RESTful APIs connect mobile apps, web services, and IoT devices."
                summary = "REST is a standard way to build APIs using HTTP methods."
            elif any(k in dl for k in ["cookie", "session", "stateful"]):
                examples = [
                    "Shopping cart items persist via session cookies until checkout.",
                    "Login tokens stored in cookies enable persistent authentication."
                ]
                keywords_list = ["cookies", "sessions", "authentication", "tokens"]
                industry = "E-commerce and SaaS rely on cookies/sessions to manage user state."
                summary = "Cookies store client data; sessions store server-side user state."
            elif any(k in dl for k in ["mvc", "mvvm", "architecture", "pattern"]):
                examples = [
                    "Model stores data, View displays it, Controller handles user input.",
                    "MVVM separates UI logic from business logic for testability."
                ]
                keywords_list = ["MVC", "Model", "View", "Controller", "separation of concerns"]
                industry = "MVC architecture structures large web applications for maintainability."
                summary = "MVC separates concerns: data, presentation, and logic."
            elif any(k in dl for k in ["cors", "cross-origin", "same-origin"]):
                examples = [
                    "Frontend on domain A accessing API on domain B requires CORS headers.",
                    "Browsers enforce same-origin policy for security unless CORS allows it."
                ]
                keywords_list = ["CORS", "cross-origin", "same-origin policy", "headers"]
                industry = "Modern web requires CORS for secure cross-domain communication."
                summary = "CORS allows controlled access to resources from different origins."
            elif any(k in dl for k in ["request", "response", "http"]):
                examples = [
                    "A browser sends a GET request to fetch a web page.",
                    "A form submission sends a POST request with user data to the server."
                ]
                keywords_list = ["HTTP", "request", "response", "status codes"]
                industry = "HTTP is the foundation of web communication."
                summary = "HTTP request-response cycle enables all web transactions."
            else:
                examples = [
                    "Building interactive user interfaces that respond to user input.",
                    "Creating scalable backend services that serve millions of users."
                ]
                keywords_list = ["web", "browser", "server", "ui", "database"]
                industry = "Web development powers the modern internet and digital transformation."

        elif subject == "Artificial Intelligence":
            definition = (
                "Artificial Intelligence (AI) is the field of creating intelligent machines that can learn, reason, and make decisions."
            )
            if any(k in dl for k in ["machine learning", "ml"]):
                examples = [
                    "Spam detection in email learns from labeled spam and legitimate emails.",
                    "Movie recommendations learn user preferences from viewing history."
                ]
                keywords_list = ["supervised", "unsupervised", "training", "model"]
                industry = "ML powers fraud detection, recommendation systems, and predictive analytics."
                summary = "Machine learning enables systems to improve without explicit programming."
            elif any(k in dl for k in ["supervised", "unsupervised"]):
                examples = [
                    "Supervised: predicting house prices from historical sales data.",
                    "Unsupervised: clustering customers by shopping behavior patterns."
                ]
                keywords_list = ["labeled data", "clustering", "classification", "regression"]
                industry = "Supervised learning dominates engineering; unsupervised helps discover patterns."
                summary = "Supervised learning uses labels; unsupervised discovers hidden patterns."
            elif any(k in dl for k in ["overfitting", "underfitting", "generalization"]):
                examples = [
                    "Model scoring 99% on training data but only 60% on test data (overfitting).",
                    "Model too simple, scoring 70% on both training and test data (underfitting)."
                ]
                keywords_list = ["overfitting", "underfitting", "regularization", "cross-validation"]
                industry = "Managing overfitting/underfitting is crucial for production ML systems."
                summary = "Balance model complexity: too simple (underfitting), too complex (overfitting)."
            elif any(k in dl for k in ["cluster", "clustering", "k-means"]):
                examples = [
                    "Customer segmentation clustering groups similar shoppers for targeted marketing.",
                    "Document clustering organizes research papers by topic similarities."
                ]
                keywords_list = ["clustering", "k-means", "similarity", "centroid", "unlabeled"]
                industry = "Clustering discovers hidden customer segments and market opportunities."
                summary = "Clustering groups similar data points without labels; use for exploration."
            elif any(k in dl for k in ["activation", "relu", "sigmoid", "tanh"]):
                examples = [
                    "ReLU in hidden layers allows networks to learn non-linear relationships.",
                    "Sigmoid in output layer constrains predictions to probability [0, 1]."
                ]
                keywords_list = ["activation function", "ReLU", "sigmoid", "non-linearity"]
                industry = "Activation functions are critical for deep learning to work well."
                summary = "Activation functions introduce non-linearity enabling neural networks to learn complex patterns."
            elif any(k in dl for k in ["neural", "deep learning", "neural network"]):
                examples = [
                    "Deep learning powers image recognition in Google Photos.",
                    "Neural networks enable voice assistants like Alexa to understand speech."
                ]
                keywords_list = ["neural network", "layers", "backpropagation", "activation functions"]
                industry = "Deep learning dominates computer vision, NLP, and autonomous systems."
                summary = "Neural networks with many layers enable learning complex patterns."
            else:
                examples = [
                    "Natural language processing enabling chatbots to understand questions.",
                    "Computer vision helping autonomous vehicles detect objects."
                ]
                keywords_list = ["AI", "learning", "intelligence", "automation"]
                industry = "AI is transforming every industry from healthcare to finance to transportation."

        elif subject == "Software Engineering":
            definition = (
                "Software Engineering is the systematic process of planning, designing, building, testing, and maintaining software systems."
            )
            if any(k in dl for k in ["sdlc", "phases", "lifecycle"]):
                examples = [
                    "Waterfall: planning -> design -> coding -> testing -> deployment.",
                    "Agile: iterative sprints with continuous feedback and improvement."
                ]
                keywords_list = ["planning", "design", "implementation", "testing", "deployment"]
                industry = "SDLC models guide software projects from inception to maintenance."
                summary = "SDLC phases ensure systematic, organized software development."
            elif any(k in dl for k in ["design pattern", "pattern"]):
                examples = [
                    "Singleton pattern ensures only one instance of a database connection.",
                    "Factory pattern creates objects without specifying exact classes."
                ]
                keywords_list = ["design pattern", "reusable", "best practices", "architecture"]
                industry = "Design patterns reduce complexity and improve code maintainability."
                summary = "Design patterns are proven solutions to common engineering problems."
            elif any(k in dl for k in ["version control", "git", "svn"]):
                examples = [
                    "Git enables teams to collaborate, tracking all code changes over time.",
                    "Branches allow parallel development of features before merging."
                ]
                keywords_list = ["version control", "git", "commit", "branch", "merge"]
                industry = "Version control is essential for multi-person software teams."
                summary = "Version control tracks code history, enables collaboration and rollback."
            elif any(k in dl for k in ["unit test", "testing", "test-driven"]):
                examples = [
                    "Unit tests verify individual functions work correctly.",
                    "Test-driven development writes tests before implementation."
                ]
                keywords_list = ["unit test", "TDD", "assertion", "mock", "coverage"]
                industry = "Testing ensures code quality and reduces production bugs."
                summary = "Unit tests catch bugs early; test-driven development improves design."
            elif any(k in dl for k in ["ci", "cd", "continuous"]):
                examples = [
                    "CI/CD pipelines automate building, testing, and deploying code on every commit.",
                    "Jenkins orchestrates testing and deployment workflows."
                ]
                keywords_list = ["CI/CD", "continuous integration", "deployment", "pipeline"]
                industry = "CI/CD enables rapid, reliable software delivery."
                summary = "CI/CD automates testing and deployment for faster, safer releases."
            elif any(k in dl for k in ["agile", "scrum"]):
                examples = [
                    "Sprints of 2 weeks with daily standups and regular demos.",
                    "User stories and backlog prioritization for continuous delivery."
                ]
                keywords_list = ["agile", "scrum", "sprint", "backlog", "iteration"]
                industry = "Agile dominates modern software development across tech companies."
                summary = "Agile enables rapid feedback and continuous improvement."
            else:
                examples = [
                    "Planning large projects with clear requirements and timelines.",
                    "Testing and debugging software to ensure reliability."
                ]
                keywords_list = ["software", "engineering", "quality", "process"]
                industry = "Software engineering practices separate hobby coding from professional development."

        elif subject == "Compiler Design":
            definition = (
                "Compiler Design covers the theory and practice of translating source code into machine-executable instructions."
            )
            if any(k in dl for k in ["lexical", "tokenization", "token"]):
                examples = [
                    "Converting 'int x = 5;' into tokens: INT, IDENTIFIER, ASSIGN, NUMBER.",
                    "Building a symbol table to track variable names and types."
                ]
                keywords_list = ["lexical analysis", "tokenization", "scanner", "lexeme"]
                industry = "Lexical analysis is the first phase in every compiler."
                summary = "Lexical analysis breaks source code into meaningful tokens."
            elif any(k in dl for k in ["parser", "parsing", "syntax"]):
                examples = [
                    "Parser checks if statement is: 'if (condition) { body }'.",
                    "Building a parse tree to represent code structure."
                ]
                keywords_list = ["parsing", "syntax", "grammar", "parse tree"]
                industry = "Parsers enforce language syntax rules."
                summary = "Parser analyzes token sequence to build syntactic structure."
            elif any(k in dl for k in ["semantic", "type check", "scope"]):
                examples = [
                    "Type checker ensures 'int x = \"hello\";' is caught as an error.",
                    "Scope checker ensures variables are declared before use."
                ]
                keywords_list = ["semantic analysis", "type checking", "scope", "symbol table"]
                industry = "Semantic analysis prevents type errors and undefined variables."
                summary = "Semantic analysis validates meaning; catches errors before code generation."
            elif any(k in dl for k in ["symbol table", "symbol", "scope", "binding"]):
                examples = [
                    "Symbol table tracks variable name, type, scope, and memory address.",
                    "Scope resolution: inner scope variable shadows outer scope variable."
                ]
                keywords_list = ["symbol table", "scope", "binding", "lookup", "resolution"]
                industry = "Symbol tables are crucial for managing variable visibility and type information."
                summary = "Symbol tables track variable metadata across scopes for type safety."
            elif any(k in dl for k in ["intermediate", "representation", "ir", "ir code"]):
                examples = [
                    "IR: 'x = a + b' becomes: t1 = LOAD a; t2 = LOAD b; t3 = ADD t1, t2; STORE t3, x.",
                    "IR enables platform-independent optimization before code generation."
                ]
                keywords_list = ["intermediate representation", "IR", "optimization", "portable"]
                industry = "IR allows compilers to optimize code independently of target platform."
                summary = "Intermediate representation bridges source code and machine code."
            elif any(k in dl for k in ["code generation", "codegen"]):
                examples = [
                    "Translating 'x = a + b' into assembly: load a, add b, store x.",
                    "Optimizing loops for faster execution."
                ]
                keywords_list = ["code generation", "assembly", "optimization", "machine code"]
                industry = "Code generation determines final program performance."
                summary = "Code generation translates optimized intermediate code to machine instructions."
            else:
                examples = [
                    "Translating high-level language to machine instructions.",
                    "Optimizing compiler output for speed and memory efficiency."
                ]
                keywords_list = ["compiler", "compilation", "translation", "optimization"]
                industry = "Compilers are fundamental tools enabling all software development."

        elif subject == "Discrete Mathematics":
            definition = (
                "Discrete Mathematics studies mathematical structures with distinct, separate values used in computer science."
            )
            if any(k in dl for k in ["set", "set theory", "operations"]):
                examples = [
                    "Set of all prime numbers: {2, 3, 5, 7, 11, ...}",
                    "Union of students in CS: all students in all CS sections."
                ]
                keywords_list = ["set", "union", "intersection", "subset", "complement"]
                industry = "Set theory foundations computer database design and logic."
                summary = "Sets organize elements; operations like union process them."
            elif any(k in dl for k in ["graph", "graph theory", "vertex", "edge"]):
                examples = [
                    "Social network: people are vertices, friendships are edges.",
                    "City map: intersections are vertices, roads are edges."
                ]
                keywords_list = ["graph", "vertex", "edge", "path", "connected"]
                industry = "Graph theory powers networking, recommendation engines, and routing."
                summary = "Graphs model relationships; algorithms traverse or optimize them."
            elif any(k in dl for k in ["boolean", "boolean algebra", "logic"]):
                examples = [
                    "Boolean expression: (A AND B) OR NOT(C) simplifies circuit logic.",
                    "Truth table shows all possible inputs and outputs for a Boolean function."
                ]
                keywords_list = ["Boolean algebra", "AND", "OR", "NOT", "truth table"]
                industry = "Boolean logic is the foundation of digital circuit and CPU design."
                summary = "Boolean algebra simplifies logic; gates implement Boolean operations."
            elif any(k in dl for k in ["logic gate", "gate", "circuit"]):
                examples = [
                    "AND gate: output 1 only if both inputs are 1.",
                    "OR gate: output 1 if at least one input is 1."
                ]
                keywords_list = ["logic gate", "AND", "OR", "NOT", "NAND", "circuit"]
                industry = "Logic gates are building blocks of all digital computers."
                summary = "Logic gates implement Boolean operations; combined they form circuits."
            elif any(k in dl for k in ["induction", "mathematical induction", "proof"]):
                examples = [
                    "Prove 1 + 2 + ... + n = n(n+1)/2 by induction over n.",
                    "Base case: n=1 works. Inductive step: if true for n, prove for n+1."
                ]
                keywords_list = ["mathematical induction", "base case", "inductive step", "proof"]
                industry = "Mathematical induction proves properties over infinite sequences."
                summary = "Induction proves statements by establishing base case and inductive step."
            elif any(k in dl for k in ["combinatorics", "probability", "permutation", "combination"]):
                examples = [
                    "Permutations: arranging 3 books in different orders.",
                    "Probability: chance of drawing a specific card from a deck."
                ]
                keywords_list = ["combinatorics", "probability", "factorial", "expected value"]
                industry = "Probability and combinatorics underpin cryptography and algorithms."
                summary = "Combinatorics counts arrangements; probability measures uncertainty."
            else:
                examples = [
                    "Logic and reasoning problems solved using discrete structures.",
                    "Counting problems using combinatorics and permutations."
                ]
                keywords_list = ["discrete", "mathematics", "logic", "counting"]
                industry = "Discrete math is essential for algorithm analysis and computer science."


    # Nicely format the response with conditional sections
    resp = [intro]
    resp.append(f"<h3>Definition</h3><p>{definition}</p>")
    if examples:
        resp.append(f"<h3>Real-world Examples</h3>{make_list(examples)}")
    if industry:
        resp.append(f"<h3>Industry Application</h3><p>{industry}</p>")
    if keywords_list:
        resp.append(f"<h3>Important Keywords</h3>{make_list(keywords_list)}")
    if summary:
        resp.append(f"<h3>Short Summary</h3><p>{summary}</p>")

    footer = (
        "<p class=\"response-footer\">"
        "Feel free to refine your question or ask for a concrete example; I'm happy to help further!"
        "</p>"
    )
    resp.append(footer)

    return "\n".join(resp)


@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    selected_branch = "Computer Science"
    selected_subject = "Data Structures"

    if request.method == 'POST':
        selected_branch = request.form.get('branch', 'Computer Science')
        selected_subject = request.form.get('subject', 'Data Structures')
        doubt = request.form.get('doubt', '')
        response = get_response(selected_branch, selected_subject, doubt)

    return render_template(
        'index.html',
        response=response,
        branch=selected_branch,
        subject=selected_subject,
        branch_subjects=BRANCH_SUBJECTS,
        sample_doubts=SAMPLE_DOUBTS,
    )


if __name__ == '__main__':
    app.run(debug=True)
