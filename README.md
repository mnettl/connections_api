## connections_api

This is an unofficial API for archived Connections word games.

---

## Endpoints

The API has four endpoints. You can access a whole puzzle by puzzle number or date, just the 16 words, or just answers. 

### URLS

- **get puzzle by number** - puzzles/[puzzle number] 
  - **get words only** - puzzles/[puzzle number]/words
  - **get answers only** - puzzles/[puzzle number]/answers
-  **get puzzle by date** - puzzles/?date=YYYYMMDD

### Examples

#### Get puzzle by number - puzzles/[puzzle number]
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

#### Get words only - puzzles/[puzzle number]/words

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

#### Get answers only - puzzles/[puzzle number]/answers

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

#### Get puzzle by date - puzzles/?[date]

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

