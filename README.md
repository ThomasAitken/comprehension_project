# comprehension_project
Simulating Understanding of English language sentences; Paraphrases of Events; Combining Machine Learning + Symbolic Techniques Influenced by Cognitive Linguists.

I am working on a few things:

  (1.) Parsing/decomposing sentences in several different ways, via techniques both simple and complicated:
      (a) on each novel phrase/sentence, using (for now, at least) the Spacy 'large' English NLP model to determine parts of speech and measure similarity between words/phrases and categories in a basic ontology (at first, just an ontology of noun-mapped entities, but hoping to create a small ontology of verb-mapped entities). Purpose: creating a massive database of concepts which could be turned ultimately into a sort of 'meaning graph' (see (2.) for more)
      (b) using a constituency parser pipe to this model so I can extract deeper syntactic information in order to see what is acting on what, what is modifying what, etc. Mixture of semantic/syntactic hopefully should allow me to distinguish e.g. predication from a verb phrase describing a process. (I don't understand and fear 'dependency parsing' so I am set on constituency parsing, which I am inclined to believe is much more powerful.) I have some background in linguistics fortunately...

  (2.) Creating a pipeline to a SQL database with a bunch of tables containing endless lists of concepts properly labelled and encoded for easy retrieval. (Working on algorithm to try to test for every new noun or verb whether it has seen 'the same word' before (very aware of polysemy in language and trying to work around it by averaging word-level and phrase-level similarity scores - definitely work in progress).) Considering setting up a pipeline to a database storing information about specific agents and one containing information about specific events, etc. Definitely need to memorise this information in some format - hugely powerful.
  
  (3.) Working on creating a system whereby semantic/syntactic information (ontological classification of words, etc), and database info, and other remembered info, all combined into deep meaning-extraction system which identifies what EVENTS have occurred in what SETTINGS, which AGENTS were involved therein, what static properties these AGENTS have, what STATES existed at time t_0 and what states exist at time t_1, and so on... The nearest actionable and useful tool to come out of such a system, if I am able to significantly develop it, would be paraphrasing of long narrative texts into a set of descriptions of the key events (I also have ideas about how to identify 'importance/significance' from semantic info), with searchable info about properties of key players and state changes undergone..

First self-set benchmark is to successfully break up and paraphrase several texts pitched at the level of young children - then work my way up to simple-English short stories by authors like Raymond Carver, Hemingway, perhaps others (generally, trying to avoid free indirect style and want to stick to fiction that makes it relatively clear what is a thought, what is speech, what is description).

This is ultimately a 'general intelligence'-style project. Which is not to say I don't see that this kind of approach to meaning is inherently and necessarily constrained; any system which can approximate the richness of our meaning representations will likely need to interact with some kind of rich world (virtual/real) with physics and complex environmental changes... As I've written somewhere in some of the project notes, I imagine that the big semantic graph and basic ontological equipment that would ideally come out of this project could be a launching pad for training an agent to develop richer representations of these ontological constituents in some virtual-reality world where all entities are labelled (so that there is a bridge from text to richer, higher-dimensional representations of entities, beyond their structural similarity to other entities and onto something more 'tangible').

## Progress to date:
Project remains messy but a concrete few things have been developed now (nothing too fancy, working slowly).

* Set up basic requirements for loading data into database (but no data being produced as yet)
* Developed a relatively simple decomposition/flattening algorithm for representing conceptual distance on the 2d plane (in *database/semantic_map.py*.. thought it could be of use but I think the 2d representation is untenable - need to preserve a high-dimensional representation for analysis))
* Have developed the beginnings of the first stage of the text-processing pipeline I'm developing, testing it on Hungry Caterpillar (sue me):
  * Have now completed a full, working constituency parse prototype.
  * Have implemented a basic prototype for space/time context-tracking over the course of the narrative and set up the system whereby events are represented (in JSON).

