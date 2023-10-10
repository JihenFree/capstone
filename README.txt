# Excerpts Brought to Light

_Exerpts Brought to Light_ is a web app that offers an interactive catalogue of excerpts from literary books, essays, poetry or fictions, thanks to the contribution of users that can enjoy multiple functionalities and book gifts on a regular basis. It also allows any visitor to search excerpts thanks to an elborated search tool.

## Distinctiveness and Complexity

### Distinctiveness 
Unlike usual quotes' or books' web catalogue, _Exerpts Brought to Light_ web app is focused only on excerpts from books. Excerpts are automatically filtered and so displayed by genre if wanted. It also allows users to search excerpts by typing the author name, the book title or any word from the excerpt.

 _Exerpts Brought to Light_ also offers functionalities and fun features that make it not only interesting to visit but also very encouraging for registered users to contribute and stay tuned. In fact:

- Thanks to their contributions, registered users can periodically win gifts which are attributed by means of a counter. Each winning user receives a notification in order to be informed about it and to confirm or change their postal address.
- Logged in users can add excerpts they like to their "My Likes" filter, which also improves the popularity of each liked excerpt.
- The main purpose of _Exerpts Brought to Light_  is to enrich the data base with excerpts from a huge range of books through the users contributions in order to attract more visitors -- The rewards concept being a further significant motivation to engourage the users to boost the site's popularity.

### Complexity
- Each 10 posted excerpts, the user who posted the (10.n)th excerpt wins a book as a gift. That book should be chosen by the winner among a list of books that have been selected according the books of the exceprts that the user has liked the most.
- The winner receives a notification to be informed about their reward and to click a link that displays a form were he is invited to choose a book among the suggested selection of books based on the exceprts from the books that they have liked the most. They are also invited to check or edit their postal address and confirm it.
- If a user is successively twice the (10.n)th poster, no gift is attributed until the next 10(n+1)th posted excerpt.
- Every user can't post more than 3 excerpts per day. At the 4th attempt, a message informing that the daily limit has been reached is diplayed.
- Users and visitors can search excerpts by typing a word from the excerpt, the title or the author name, as the user types their search word, onkeyup the search input provides a dropdown list of suggestions from the database, before the user clicks the "Find" button.
- Users can click the like button on an excerpt which adds the liked excerpt to their "My Likes" excerpts list as well as it increases the number of likes and so the popularity of that excerpt.
- Users and visitors can toggle display of excerpts between chronological order and order by popularity (number of likes).
- Users and visitors can click on the author name and book title on any excerpt to display only the excerpts from the clicked book title or author name in the active page.
- Registered users can display the list of the excerpts they posted and have the possibility to edit or delete them.

## Files
### static
#### _excerptscript.js_
 _excerptscript.js_ is a java script file that contains functions to do operations either at content load or at clicking certain buttons which allowed to assemble most of the functionalities of the web app in the _index.html_ page. The major functions are :
 
 - _***document.addEventListener('DOMContentLoaded', function()***_ is launched when page is loaded. it changes the Poetry and Fiction excerpts style by changing their class. It also handles the _Search_ fonctionality via a function that is enabled _onkeyup_ while typing the word in the search input -- Then a fetch request is sent through the _search_ path to _views.search_ to obtain a drop down list of suggestions containing the typed word that is generated from data base and delivered in _json response_  .
- _***newExcerpt()***_ is enabled when the _New Excerpt_ button is clicked. It activates the modal display form that contains the input fields to create a new excerpt. It also sends a fetch request to _views.maxday_ in order to check the daily allowed number of exceprts posted by the user; and displays a message informing they've reached the daily limit and so not allwing them to post more exceprts until the next day.
- _***editExcerpt***_ is called when the quill icon in a user's authenticated excerpt is clicked. It displays a form filled with the excerpt's information in order to be edited by changing either the text, the book title, the author name or the genre of the book. It allows users to correct any mistakes in their own posted excepts.
- _***savedit***_ it is called when the button _save_ of the form _Edit excerpt_ is clicked. It first gathers the inputs of the form's fields (excerpt text, author name, and book title) and displayes them in the edited excerpt. Then it send a fetch request with POST method to views.edit in stringified JSON data in order to be saved in data base.
- _***like***_ is called when the heart icon under an excerpt is clicked. It changes the icon image from grey heart to a golden heart; but it also sends a fetch request to _views.likes_ to add the user's like to database but also to receive a json response that allows to update the display of total likes number of the liked excerpt.
- _***alertDelete***_ & _***deletethis**_ the formal is an alert that is displayed when the cross icon on top of a user's own excerpt is clicked. It warns the user about deletion by asking for confirmation. Once "Yes" is clicked, _deletethis_ function is called it send a fetch request to _views.delete_ in order to delete the excerpt from data base.
- _***navtab***_ changes the active tab according to the nav-link that is clicked. The tab that is active by default when the index page is loaded is the _All_ tab which displays all types of excerpts strating from the most recently posted. 
- _***byauthor***_ &  _***bybook***_ is called when respectivley the author name or the book title of an excerpt is clicked. It allows to display on the current page only the excerpts from the book or the author that was  clicked.
- _***confirmReward***_ is called when the link in he notification informing the authenticated user that they had won a reward. I diplays a form where the user must chose the book they want to receive and confirm. The books that are suggested  are displayed in a drop don list that is generate via the fetch request in this function. The fetch request is sent to _views.booklist_ in order to gather their favorite books in json response from the _TopBook_ model in data base.
-  _***saveReward***_ is called when the button "Submit" in the form above is clicked. Once the user chooses from the drop down list the book they want to receive as a reward, they click "Submit" to confirm, and the form data including the chosen book and the updated address that the user had input is submitted by POST method via a fetch request to _views.complete_reward_ to be stored in data base
- _***unsentRewards***_ is called when the superuser, who is in charge of managing the rewards, clicks the link in the notification they receive when there are rewards in the database that haven't been sent to their winners yet. It sends a fetch request to _views.rewardlist_ to get the unsent rewards from database in json response and display them in a drop downlist in order to pick one.
- _***detailReward***_ is called when a book from the list of the unsent rewards above is selected. It It sends a fetch request to _views.reward_ and receives in json response the details of the selected book from the data base in order to add change the "sent" status and to add the shipment details.



#### _styles.css_
Due to the use of a Bootswatch theme for the style design of this web app, the CSS file contains mainly the body style with the definition of the background and the margins.

### templates
#### _layout.html_

It contains the overall design of the web app. It consists of :
* the links in the header to the bootswatch theme files and the CSS and JS files.
* the navbar which contains the header that is also a link to the index page itself, the nav links that are "Register" and "Login" if the user is not authenticated; and are "New Excerpt" and "Log out" if the user is. The "New Excerpt" nev link calls the JS _newExcerpt_ function.
* The style attributes of the navbar makes it mobile-responsive thanks to ``` display: flex;flex-wrap: wrap;```

#### _register.html_ 

It contains a form with 4 fields where the user should input their user name, their email address, their password and the confimation of their password. If the usersame already exists or the password confirmation doesn't match the typed password, the field frame turns to red, a red warning signal appears inside the field and a red error message appears below the field in question.
#### _login.html_ 

It contains a form with two inputs where the user types their user name and their password to be authenticated.

#### _index.html_ 

It is the home page and it contains, thanks to Javascript, most functionalities of the web app.

**The default display** shows all the excerpts posted in a chronologically descending order. These excerpts are displayed in the default _All_ tab-pane while other tab-panes are accessible by the genre of the books from which the excerpts are taken. There are three genres and so three other tab-panes which nav-links are :  _Fiction_, _Philosphy_, and _Poetry_. Once one of these nav-links is clicked, the corresponding nav-tab containing the excerpts from books of the selected genre is activated and so the filtered exceprts only are displayed. in all the panes excerpts are arranged in a grid layout.

**the display of the excerpts is mobile-responsive** thanks to the flex properties defined in the style of the tab panes : ``` flex-wrap: wrap;
      display: inline-flex;```

**Each excerpt** is framed with a border in a card design; and inside each excerpt card there is the text of the excerpt, the book title from which the excerpt was taken and the author name. The book title and the author name are also links that activate respectively the JS functions _bybook(this)_ & _byauthor(this)_ and so displays only the excerpts from the clicked book title ot the clicked author name that exist on the current page. Theres is also in the left bottom corner of the card the heart icon for liking the excerpt, and in the right bottom corner there is the total number of likes for that excerpt. When the grey heart is clicked by a non autenticated user, the user is directed to the login page. 

**The search field** is for finding excerpts by typing either the book title, the author name or any word or phrase from the excerpt. Once the _Find_ button is clicked, twenty excerpts among the results are displayed randomly. Also while typing the search words, a dropdown list appears with suggestions containing the typed strings.

**Pagination** at the bottom of the page displays the number of pages. Each clicked number loads the excerpts of that page. Each page containing 20 excerpts. The first and last arrows in the pagination items are respectively the _next_ and _previous_ page of the current page. 

**Authenticated users display** is a bit different. The Nav bar items change to _New Excerpt_ and _logout_ and the username appears under the Nav bar on the left. There are two more nav tab items _My Excerpts_ and _My Likes_. 

**My Excerpts** pane contains the excerpts the authenticated user created but with different icons. At the top right corner of each excerpt there is a cross which deletes the excerpt when it's clicked after poping up a deletion confirmation alert. At the bottom left corner there is the quill icon that is for editing the excerpt content. When it's clicked a form window pops up it contains a textarea filled with the excerpt, two input fields one with the book title and the other with the author name, and a select field to change the genre.

**My Likes** pane displays the excerpts that the user has liked.

**New Excerpt** pops up a form window containing a textarea for the excerpt text, an input for the author name and an input for the book title and a select dropdown list to choose the genre option.When the save botton is clicked, the index page is loaded with the new excerpt on top. 

**Congratulations** alert is displayed when  an authenticated user that isn't the last winner  has posted an excerpt having an id that is a multiple of 10. The message congratulates the winner and contains a link to update and confirm their adress and to choose the book they want to receive as a reward.

**Reward** window opens when the link in the congratulation alert is clicked. It prompts the user to choose their reward from the select list of books that were picked -according to the user's likes- from the _TopBook_ model. Rhe user can also change their address in the text area where it is displayed and editable, then confirm by clicking the _submit_ button. Once done, an alert greating the user is displayed.

**Unsent Rewards** alert is displayed if the _SuperUser_ is authenticated and if there are unsent rewards, in order to inform them the rewards that haven't been sent to their winners. It contains a link that opens a modal where the superuser can select an unsent reward from the droplist. once a reward is selected the details of the selected reward are displayed : the winner username, the book title and author, the reward N°, the reward date which is the date when winner posted the excerpt that made him win, and the winner's address.

**Maximum daily excerpts by user** alert is diplayed when a user tempts to post more than 3 posts per day, informing them that they have reached their daily allowed maximum number of excerpts to be posted.

### Python Files

#### views
**index(request)** returns _index.html_ on the first page  with the 20 most recent posted excerpts and the _All_ pane activated.

**oldpages(request, this_page)** takes this_page as argument and returns _index.html_ containing the 20 excerpts of the page number _this_page_ 

**bylikes(request)** orders exerpts by popularity with most liked excerpts on top. it returns _index.html_ with the 22 most liked excerpts. Only liked experpts are displayed. Exerpts with 0 likes aren't.

**search(request, word)** is activated when a word is typed in the search field. it takes the typed word as argument and filters in the _Excerpt_ model the objects that contain the typed word in the book and the author fields. It returns a JsonResponse of the serialized objects of the search results. The author and book names from those results will be displayed in a dropdown list.

**find(request)** is activated by the POST method from the form submitted by clicking on the _Find_ button. It returns _index.html_ with 23 excerpts picked randomly from the search results of excerpts containing the typed word or phrase in the book field, the author field ot the text field of _Excerpt_ model.

**login_view(request)** is activated when the user clicks on the _login_ item in the navbar, so it loads the _login.html_ file. Or by POST method if the user click the _Login_ button in the login form; if the typed username or password aren't correct, a message is displayed to inform the user.

**logout_view(request)**

**register(request)** is activated when the user clicks the _Register_ nav item the navbar, so it loads the file _register.html_ or via POST method in the following cases :
- if the typed password is not the same as the typed confirmation password. In this case a message about password is displayed and the confirmation password fied is framed in red with a red warning symbol inside.
- if the username already exists in the database. In this case a message about username is displayed and the username field is framed in red with a red warning  symbol inside.


**new_excerpt(request)** is activated by the POST method from the _New Excerpt_ form. it creates a new Excerpt object in the _Excerpt_ model by introducing the excerpt's text, the book title, the author name, and the creation date and time. It also checks the id of the user who created the new excerpt, and the last rewarded user in the _Reward_ model. if the id of the created excerpt is a multiple of 10 and the id of the user is different from the last winner, the user is added to the winners list by creating a new _Reward_ object in the _Reward_ model, introducing the user object and the date.

**maxday(request)** is activated when maximum allowed number of posted excerpts per day for a user is reached. It returns a JasonResponse containing the number of excerpts for the NewExcerpt js function in order to display an alert if the maximum number is reached.

**delete(request, excerpt_id)** is activated when the cross on top right corner of the exerpt is clicked and the alert message confirmed. it deletes the excerpt with the id _excerpt_id_ 

**edit(request, excerpt_id)** is activated when the save button in the excerpt edit form is clicked. It takes as argument the excerpt id, and it collects json stringified data containing the modified text, book title, author and genre of the edited excerpt via POST method, and it saves the modified object in _Excerpt model_.
 
**likes(request, excerpt_id)** it takes the excerpt id as argument and is activated when the user clicks the heart icon to like an excerpt. The user is added to the _likes_ field in the _Excerpt_ model if it isn't found in the _likes_ of that excerpt. Else it is removed from _likes_. Once the user is added or removed from the likes.
 The excerpts liked by that user are ordered by the bigger number of likes for excerpts from the same book. If the book title of the first excerpt from the ordered list exists in the field title_topbook in the model _TopBook_ and if that _TopBook_ object hasn't that user in the user_topbook field, then that user is added there. If the _TopBook_ object doesn't exist, a new _TopBook_ object is created with the title and the author of the book in the ordered list, and the user is added to the user_topbook field in the _TopBook_ model.

**booklist(request)**  is activated when the _click here_ link in the congratulation note is clicked to generate the select drop down list of top books of the winning user in the confirm reward form. From _TopBook_ model, it filters the objects having current user in _user_topbook_ field. It returns serialized objects from the result list in JsonResponse for the fetch request to display the topbooks of the user in the confirm reward form.

**complete_reward(request, reward_id)** is activated when the _submit_ button in the _Your Reward_ form. Once the user has chosen their reward and updated their address, the data containing the book id in _TopBook_ model and the address is sent via POST method. It takes the id of the reward as argument. The book information is  collected with the TopBook id of the chosen book as a reward, then it is saved in the fields _reward_book_ and _reward_author_ in the_ Reward_ model, and it saves the address in the _User_ model.

**rewardlist(request)** is activated when the link _click here_ in the _Unsent Reward_ window, that is displayed for the Superuser when there are unsent reward, is clicked. In the model _Reward_, it filters the objects whose  _reward_sent_ value is _False_. It returns serialized objects from the result list in JsonResponse for the fetch request to display the unsent rewards in the Unsent Rewards window.

**reward(request)** is activated when the superuser clicks the buttons _See details_ in the _Unsent Rewards_ window once they have chosen the reward they will send to the winner.The reward_id is received in Json form by POST method. The object from the model Reward is picked with the obtained rewad is and it returns a JsonResponse of the serialized reward data.

**sending(request)** is activated when the superuser clicks on the _Save_ button in the _Unsent Rewards_ window. it receives, by POST method, the information about the sent reward : reward id, sent status, and traking number. it saves them in the corresponding object and returns the index page.

#### models
**User(AbstractUser)** in addition to username, email and password, the address which is a CharField  is added to the abstractuser default fields.
 
 **Excerpt(models.Model)** 
 
 _Excerpt_ is the model that contains the data of all the excerpts that were created. It has the following fields :
 
 * user_excerpt = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userexcerpt") is the user object that created the excerpt.
 *  excerpt_date = models.CharField(max_length=64) is the date of creation of the excerpt.
 *  excerpt_text = models.CharField(max_length=255) is the text of the excerpt.
 *  author = models.CharField(max_length=64) is the author name of the book from which the excerpt is taken.
 *  book = models.CharField(max_length=64) is the title of the book from which the excerpt is taken.
 *  genre = models.CharField(max_length=64) is the genre of the book from which the exerpt is taken.
 *  likes = models.ManyToManyField("User", related_name="likes") are users objects that have added a like to the excerpt. It's a many to many field so each user has likes field with the excerpts they liked.
 
**TopBook(models.Model)** 

TopBook is the model that contains the data of books of the excerpts that were liked. Every time a user likes an excerpt, a TopBook is created. It is defined by the title of the book from which the exceprt is taken and the author name of that book, and the user that liked it is added to the list of the users that have liked it too. These are it fields :

* user_topbook = models.ManyToManyField("User", related_name="usertopbook") are the users that have this book (TopBook object) in their top books. It's a many to many field so each user has a topbook field with the books from where the excerpts they liked are taken.
* title_topbook =models.CharField(max_length=64) is the title of the book of the excerpt that is liked ny the user and added to their TopBooks.
* author_topbook =models.CharField(max_length=64) is the author name of the book.

**Reward(models.Model)** 

_Reward_ is the model that contains the data of rewards that were attributed to users having posted excerpts whose id is a multiple of 10. it is defined by the following fields :

* user_reward = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userreward") is the user object to which the reward is attributed.
* reward_date = models.CharField(max_length=64) is the date of creation of the reward in the data base which correponds to the date when the excerpt wth an id that is multiple of ten was created.
* reward_book = models.CharField(max_length=64) is the title of the book that the user has chosen in the user has chosen among their Top books list as suggested in the _Your Reward_ form.
* reward_author =  models.CharField(max_length=64) is the author name of the selected book.
* reward_sent = models.BooleanField(default=False) is a boolean field that informs about whether the reward was sent (true) or not (false).
* ship_track =  models.CharField(max_length=64,default="no shipping") contains tracking number and shipper company name.

#### urls

The following urls are paths to views that return html pages. These were explained along with the description of the content of the html files.

    path("", views.index, name="index"),
    path("oldpages/<int:this_page>", views.oldpages, name="oldpages"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newexcerpt", views.new_excerpt, name="newexcerpt"),
    path("find", views.find, name="find"),
    path("bylikes", views.bylikes, name="bylikes"),
    path("sending", views.sending, name="sending"),


The following paths are API Routes that called via fetch request in a JS function. Most of them return Json Responses. These were axplained in the description of the content of the JS file.


    path("likes/<int:excerpt_id>", views.likes, name="likes"),
    path("edit/<int:excerpt_id>", views.edit, name="edit"),
    path("delete/<int:excerpt_id>", views.delete, name="delete"),
    path("maxday", views.maxday, name="maxday"),
    path("booklist", views.booklist, name="booklist"),
    path("rewardlist", views.rewardlist, name="rewardlist"),
    path("completereward/<int:reward_id>", views.complete_reward, name="completereward"),
    path("reward/", views.reward, name="reward"),
    path("search/<str:word>", views.search, name="search")


### How to run

In the IDE terminal under _capstone_ folder launch the command 

```sh
CD capstone
python manage.py runserver
```