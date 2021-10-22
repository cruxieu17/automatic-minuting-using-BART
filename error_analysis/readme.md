# Error Analysis
This is the Error Analysis section from the paper.

Although the proposed approach shows a satisfactory performance on the task, a few loopholes remain that leave scope for improvement. 
We analyze the meeting minutes obtained to find erroneous cases. Errors discovered during the analysis are enlisted below.

* Made-up entities - Anonymization of discreet entities in transcripts (e.g., LOCATION7, PERSON4, Marketing Manager) is a consistent practice in most organizations. Sometimes, this results in generation of made-up entities that are initially not part of that transcript. This behavior is attributed to the fact that no such anonymization methods were used while creating the Samsum dataset unlike DialogsSum and SummScreen corpuses. De-anonymizing the identities in the transcript by passing a random name corresponding to every speaker solves this trivial error satisfactorily.
* Rare absences of a topical context - This is unarguably the most intractable issue that persisted. The model, however, allows us to repair this absence by varying the token intake length of the embedded summarization model. A lesser input token-length returns a more elaborate minute.  More often than not, this issue did not appear in generated minutes as the model efficiently captured the discussions' topics. 
* Incomplete phrases - Further analysis brought to out notice some scarce occurrences of some incomplete sentences. These were generally from those parts of the transcripts where the utterances either had missing punctuation or hesitations and interruptions on the speaker's part.

![](fig.png)

