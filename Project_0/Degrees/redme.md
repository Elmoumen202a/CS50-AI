# Degrees of Separation

## Project Overview
This project implements a function `shortest_path` to find the shortest path between two individuals in the movie industry, measured in "degrees of separation." The goal is to determine the path of movies and co-stars that connects a source person to a target person in the fewest possible steps.

## Implementation Details

### `shortest_path` Function
Complete the implementation of the `shortest_path` function in the `degrees.py` file. This function takes two arguments, `source` and `target`, representing the IDs of two individuals. It returns a list of (movie_id, person_id) pairs that form the shortest path from the source person to the target person.

- Each pair in the list should be a tuple of two strings.
- If there are multiple paths of minimum length, the function can return any of them.
- If there is no possible path between two actors, the function should return `None`.
- You may use the `neighbors_for_person` function, which returns a set of (movie_id, person_id) pairs for all people who starred in a movie with a given person.

### Example Usage
```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
