from django.shortcuts import render


courses = [
    {
        "id": 1,
        "title": "Python Basics",
        "category": "backend",
        "difficulty": "beginner",
    },
    {
        "id": 2,
        "title": "Django Fundamentals",
        "category": "backend",
        "difficulty": "intermediate",
    },
    {
        "id": 3,
        "title": "HTML & CSS",
        "category": "frontend",
        "difficulty": "beginner",
    },
    {
        "id": 4,
        "title": "SQL & Databases",
        "category": "database",
        "difficulty": "beginner",
    },
    {
    "id": 5,
    "title": "JavaScript Basics",
    "category": "frontend",
    "difficulty": "beginner",
},
{
    "id": 6,
    "title": "Git & GitHub",
    "category": "tools",
    "difficulty": "beginner",
},
{
    "id": 7,
    "title": "Python OOP",
    "category": "backend",
    "difficulty": "intermediate",
},
{
    "id": 8,
    "title": "REST APIs",
    "category": "backend",
    "difficulty": "advanced",
},
]


def course_list(request):
    category = request.GET.get("category", "")
    difficulty = request.GET.get("difficulty", "")
    search = request.GET.get("search", "")
    page = request.GET.get("page", "1")

    filtered_courses = courses

    if category:
        filtered_courses = [
            course for course in filtered_courses
            if course["category"] == category
        ]

    if difficulty:
        filtered_courses = [
            course for course in filtered_courses
            if course["difficulty"] == difficulty
        ]

    if search:
        filtered_courses = [
            course for course in filtered_courses
            if search.lower() in course["title"].lower()
        ]

    try:
        page = int(page)
    except ValueError:
        page = 1

    per_page = 4
    total_pages = (len(filtered_courses) + per_page - 1) // per_page

    if page < 1:
        page = 1

    if total_pages and page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page

    paginated_courses = filtered_courses[start:end]

    return render(request, "courses/course_list.html", {
        "courses": paginated_courses,
        "category": category,
        "difficulty": difficulty,
        "search": search,
        "page": page,
        "total_pages": total_pages,
    })


def course_detail(request, id):
    course = next(course for course in courses if course["id"] == id)

    tab = request.GET.get("tab", "details")

    if tab not in ["details", "syllabus", "instructor"]:
        tab = "details"

    return render(request, "courses/course_detail.html", {
        "course": course,
        "tab": tab,
    })