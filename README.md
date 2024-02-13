## Description

This is an unofficial API for archived Connections word games.

---

## Endpoints

The API has one endpoint, ``puzzles`` . You can access a whole puzzle, just the 16 words, or just answers. 

- puzzles
	- puzzles/[puzzle number] 
		- puzzles/[puzzle number]/words
		- puzzles/[puzzle number]/answers
	- puzzles/?date=[YYYYMMDD]

### Examples
#### puzzles/[puzzle number]
```json
{
  "answers": {
    "BLUE": {
      "category_name": "RADIO LINGO",
      "category_words": "COPY, OUT, OVER, ROGER"
    },
    "GREEN": {
      "category_name": "COUNTERFEIT",
      "category_words": "BOGUS, FAKE, PHONY, SHAM"
    },
    "PURPLE": {
      "category_name": "SONGS THAT ARE NAMES",
      "category_words": "ALEJANDRO, LOLA, MICHELLE, STAN"
    },
    "YELLOW": {
      "category_name": "EYE PARTS",
      "category_words": "IRIS, LENS, PUPIL, RETINA"
    }
  },
  "puzzle_no": "95",
  "words": [
    "IRIS",
    "OUT",
    "FAKE",
    "MICHELLE",
    "COPY",
    "STAN",
    "ROGER",
    "BOGUS",
    "LENS",
    "OVER",
    "LOLA",
    "PUPIL",
    "SHAM",
    "ALEJANDRO",
    "RETINA",
    "PHONY"
  ]
}
```

#### puzzles/[puzzle number]/words

```json
{
  "puzzle_no": "95",
  "words": [
    "IRIS",
    "OUT",
    "FAKE",
    "MICHELLE",
    "COPY",
    "STAN",
    "ROGER",
    "BOGUS",
    "LENS",
    "OVER",
    "LOLA",
    "PUPIL",
    "SHAM",
    "ALEJANDRO",
    "RETINA",
    "PHONY"
  ]
}
```

#### puzzles/[puzzle number]/answers

```json
{
  "BLUE": {
    "category_name": "RADIO LINGO",
    "category_words": "COPY, OUT, OVER, ROGER"
  },
  "GREEN": {
    "category_name": "COUNTERFEIT",
    "category_words": "BOGUS, FAKE, PHONY, SHAM"
  },
  "PURPLE": {
    "category_name": "SONGS THAT ARE NAMES",
    "category_words": "ALEJANDRO, LOLA, MICHELLE, STAN"
  },
  "YELLOW": {
    "category_name": "EYE PARTS",
    "category_words": "IRIS, LENS, PUPIL, RETINA"
  },
  "puzzle_no": "95"
}
```

#### puzzles/?[date]

```json
{
  "answers": {
    "BLUE": {
      "category_name": "RADIO LINGO",
      "category_words": "COPY, OUT, OVER, ROGER"
    },
    "GREEN": {
      "category_name": "COUNTERFEIT",
      "category_words": "BOGUS, FAKE, PHONY, SHAM"
    },
    "PURPLE": {
      "category_name": "SONGS THAT ARE NAMES",
      "category_words": "ALEJANDRO, LOLA, MICHELLE, STAN"
    },
    "YELLOW": {
      "category_name": "EYE PARTS",
      "category_words": "IRIS, LENS, PUPIL, RETINA"
    }
  },
  "puzzle_no": "95",
  "words": [
    "IRIS",
    "OUT",
    "FAKE",
    "MICHELLE",
    "COPY",
    "STAN",
    "ROGER",
    "BOGUS",
    "LENS",
    "OVER",
    "LOLA",
    "PUPIL",
    "SHAM",
    "ALEJANDRO",
    "RETINA",
    "PHONY"
  ]
}
```

