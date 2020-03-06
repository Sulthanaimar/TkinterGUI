from tkinter import *
import sqlite3

root = Tk()
root.title('Project MDB')
root.geometry("1000x1000")

#make connection to db
conn = sqlite3.connect("projectmoviedb2.db")

# Create cursor
c = conn.cursor()

# Create table

# Create record delete function
def delete():
        # Create connection again inside the function (it is necessary)
        conn = sqlite3.connect('projectmoviedb2.db')
        c = conn.cursor()
        conn.commit()
        # Delete a record
        c.execute("DELETE from Movies WHERE oid = " + delete_box.get())
        delete_box.delete(0, END)
        conn.commit()

# Create submit function for DB
def submit():
        # Create connection again inside the function (it is necessary)
        conn = sqlite3.connect('projectmoviedb2.db')
        c = conn.cursor()
        conn.commit()
        # Insert into table
        c.execute("INSERT INTO Movies VALUES (:Movie, :Year, :Director, :Rating, :Synopsis)",
                {
                        'Movie': Movie.get(),
                        'Year': Year.get(),
                        'Director': Director.get(),
                        'Rating': Rating.get(),
                        'Synopsis': Synopsis.get()
                })
        # Clear text boxes
        Movie.delete(0, END)
        Year.delete(0, END)
        Director.delete(0, END)
        Rating.delete(0, END)
        Synopsis.delete(0, END)
        conn.commit()

# Create query function
def query():
        def moviedt():
                # Create connection again inside the function (it is necessary)
                conn = sqlite3.connect('projectmoviedb2.db')
                c = conn.cursor()
                conn.commit()
                nonlocal oid_label
                # Create new window for details
                top = Toplevel()
                top.title('Details')
                top.geometry("1000x1000")

                moviedtvalue = Label(top, text="Movie: ")
                moviedtvalue.grid(row=1, column=0, padx=40)
                yeardtvalue = Label(top, text="Year: ")
                yeardtvalue.grid(row=2, column=0, padx=40)
                directordtvalue = Label(top, text="Director: ")
                directordtvalue.grid(row=3, column=0, padx=40)
                ratingdtvalue = Label(top, text="Rating: ")
                ratingdtvalue.grid(row=4, column=0, padx=40)
                synopsisdtvalue = Label(top, text="Synopsis: ")
                synopsisdtvalue.grid(row=5, column=0, padx=40)
        
                c.execute("SELECT Movie from Movies WHERE oid = " + oid_label.cget('text'))
                moviesdt = c.fetchone()

                c.execute("SELECT Year from Movies WHERE oid = " + oid_label.cget('text'))
                yearsdt = c.fetchone()

                c.execute("SELECT Director from Movies WHERE oid = " + oid_label.cget('text'))
                directorsdt = c.fetchone()

                c.execute("SELECT Rating from Movies WHERE oid = " + oid_label.cget('text'))
                ratingsdt = c.fetchone()

                c.execute("SELECT Synopsis from Movies WHERE oid = " + oid_label.cget('text'))
                synopsisdt = c.fetchone()

                print_movie = ''
                for movie in moviesdt:
                        print_movie += str(movie)
                movies_label = Label(top, text=print_movie)
                movies_label.grid(row=1, column=1)

                print_year = ''
                for year in yearsdt:
                        print_year += str(year)
                year_label = Label(top, text=print_year)
                year_label.grid(row=2, column=1)

                print_director = ''
                for director in directorsdt:
                        print_director += str(director)
                director_label = Label(top, text=print_director)
                director_label.grid(row=3, column=1)

                print_rating = ''
                for rating in ratingsdt:
                        print_rating += str(rating)
                rating_label = Label(top, text=print_rating)
                rating_label.grid(row=4, column=1)

                print_synopsis = ''
                for synopsis in synopsisdt:
                        print_synopsis += str(synopsis)
                synopsis_label = Label(top, text=print_synopsis)
                synopsis_label.grid(row=5, column=1, ipadx=0)
        # Create connection again inside the function (it is necessary)
        conn = sqlite3.connect('projectmoviedb2.db')
        c = conn.cursor()
        conn.commit()
        # Query the DB
        c.execute("SELECT *, oid FROM Movies")
        movies = c.fetchall()
        print(movies)
        # Window for query
        top2 = Toplevel()
        top2.title('Query')
        top2.geometry("1000x1000")
        frame = Frame(top2)
        frame.pack()
        # Loop thru results
        #print_oid = ''
        movie_btn = []
        for movie in movies:
                movie_btn.append(Button(frame, text=str(movie[5]) + " " + "\t" + "\n", command=moviedt).pack(padx=100))

        print_oid = ''
        for oid in movies:
                print_oid += str(oid[5]) + "\n"

        #how to generate multiple buttons (please run the code first then click show movies db)
        #query_button = Button(top2, text=print_movies, command=moviedt)
        #query_button.grid(row=0, column=3, pady=20)

        #query_button = Button(frame, text=print_movies, command=moviedt)
        #query_button.pack()
        oid_label = Label(frame, text=print_oid)
        oid_label.pack()
        
# Create text boxes
Movie = Entry(root, width=30)
Movie.grid(row=1, column=1, padx=20)
Year = Entry(root, width=30)
Year.grid(row=2, column=1, padx=20)
Director = Entry(root, width=30)
Director.grid(row=3, column=1, padx=20)
Rating = Entry(root, width=30)
Rating.grid(row=4, column=1, padx=20)
Synopsis = Entry(root, width=30)
Synopsis.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=11, column=1, pady=5)

# Create text box label
Movie_label = Label(root, text='Movie')
Movie_label.grid(row=1, column=0)
Year_label = Label(root, text='Year')
Year_label.grid(row=2, column=0)
Director_label = Label(root, text='Director')
Director_label.grid(row=3, column=0)
Rating_label = Label(root, text='Rating (/10)')
Rating_label.grid(row=4, column=0)
Synopsis_label = Label(root, text='Synopsis')
Synopsis_label.grid(row=5, column=0)
delete_label = Label(root, text="Delete ID")
delete_label.grid(row=11, column=0, pady=5)

# Create submit button
submit_btn = Button(root, text="Add a Movie into DB", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Create a query button
query_btn = Button(root, text="Show MoviesDB", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a delete button
delete_btn = Button(root, text="Delete Movie", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

# Save changes
conn.commit()

# Close connection


root.mainloop()