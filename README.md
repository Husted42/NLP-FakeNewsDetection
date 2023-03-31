<<<<<<< Updated upstream
# dataScience
=======
# DataScience 

Date: 31/03/2023

<p>Extract the zip file ('news_cleaned_2018_02_13.csv') to a directory/folder, and rename it to 'csvFile.csv'.</p>
<p>Ensure that both the data and notebook pipeline are in the same directory/folder.</p>
<p>Run all cells.</p>
<p>Note that the running time may vary depending on the computer on which the pipeline is run.</p>

<p><strong>csv files:</strong></p>
<ul>
<li aria-level="1"><strong><em>csvFile.csv</em></strong>: The original dataset from fake news corpus, renamed&nbsp;</li>
<li aria-level="1"><strong><em>readyData.csv</em></strong>: The first 100k rows of <strong><em>csvFile.csv</em></strong>
<ul>
<li aria-level="1">Columns: 0, id, type, content, inserted_at, meta_description, source.</li>
</ul>
</li>
<li><strong><em>cleanedNews.csv</em></strong>: Cleaned version of <strong><em>readyData.csv </em></strong>
<ul>
<li>Result of the preprocessing section</li>
</ul>
</li>
<li><strong><em>milReadyData.csv</em></strong>: The first 5 mio rows of <strong><em>csvFile.csv</em></strong></li>
<li><strong><em>milcleanedNews.csv</em></strong>: Cleaned version of <strong><em>milReadyData.csv</em></strong>
<ul>
<li>Result of the preprocessing section&nbsp;</li>
</ul>
</li>
<li>Split of <strong><em>cleandNews.csv</em></strong>:
<ul>
<li><strong><em>split80_train.csv</em></strong></li>
<li><strong><em>split10_test.csv</em></strong></li>
<li><strong><em>split10_val.csv</em></strong></li>
</ul>
</li>
</ul>
<ul>
</ul>
<ul>
<li>Split of <strong><em>milcleanedNews.csv</em></strong>:
<ul>
<li><strong><em>milsplit80_train.csv&nbsp;</em></strong></li>
<li><strong><em>milsplit10_test.csv&nbsp;</em></strong></li>
<li><strong><em>milsplit10_val.csv&nbsp;</em></strong></li>
</ul>
</li>
</ul>
<ul>
</ul>
<ul>
</ul>
<p><strong>Sections</strong></p>
<p>Setup</p>
<ul>
<li aria-level="1">Takes <strong><em>csvFile.csv</em></strong> and gives <strong><em>readyData.csv/milReadyData.csv</em></strong> with the different amount of rows, so it&rsquo;s ready for cleaning.</li>
</ul>
<p>Data overview 1</p>
<ul>
<li aria-level="1">Data types and null count</li>
</ul>
<p>Preprocessing</p>
<ul>
<li aria-level="1">Takes the <strong><em>readyData.csv/milReadyData.csv</em></strong> through a pipeline that does: Stemming, tokenizing, and regex. And gives <strong><em>cleanedNews.csv/milcleanedNews.csv</em></strong></li>
</ul>
<p>Data overview 2</p>
<ul>
<li aria-level="1">Most used words</li>
<li aria-level="1">Word appearances&nbsp;</li>
</ul>
<p>Ready data for the baseline model</p>
<ul>
<li aria-level="1">Splitting the cleaned file into 80/10/10 randomly, so that we have one for training, test and validation.&nbsp;</li>
<li aria-level="1">Word embedding</li>
<li aria-level="1">Label to binary</li>
</ul>
<p>Data overview 3</p>
<ul>
<li aria-level="1">Scatter Plot of data</li>
<li aria-level="1">Words in wordToVec</li>
<li aria-level="1">Barchart of balance</li>
</ul>
<p>Baseline model</p>
<ul>
<li aria-level="1">Logistic regression models on the <strong><em>split80_train.csv/split10_test.csv/split10_val.csv </em></strong>files.&nbsp;</li>
<li aria-level="1">Metrics</li>
</ul>
<p>Advanced model</p>
<ul>
<li aria-level="1">Grid Search&nbsp;</li>
</ul>
<ul>
<li aria-level="1">GradientBoostingClassifer on the <strong><em>milsplit80_train.csv/milsplit10_test.csv/milsplit10_val.csv </em></strong>files.&nbsp;</li>
</ul>
<ul>
<li aria-level="1">LIAR dataset</li>
</ul>
>>>>>>> Stashed changes
