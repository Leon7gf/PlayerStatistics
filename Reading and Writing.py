# This program gets data from the user and
# saves it as records in the players.txt file
def main():
  def write():
      # Gets sport and team name + amount of stats per player.
      sport_name = input("What sport? ")
      team_name = input("What is the name of the team? ")
      amount_stats = int(input("How many stats do you want" +
                              " to include per player? "))

      # Gets name of each stat and stores it in a list
      lst_stat_name = []
      for _ in range(amount_stats):
          stat_name = input("Name statistic you want to input: ")
          lst_stat_name.append(stat_name)

      # Gets the number of players
      num_players = int(input("How many players would you like" +
                              " to input data for? "))

      # Open the file for writing
      with open("players.txt", "w") as pl_file:

          # Get each players data and writes it to the file
          for count in range(1, num_players + 1):
              print(f"Player #{count}: ")
              name = input("Player name: ")
              pl_file.write(f"{name} ({sport_name}, {team_name}):\n")

              for i in range(amount_stats):
                  stat = input(f"{lst_stat_name[i]}: ")
                  pl_file.write(f"  {lst_stat_name[i]}: {stat}\n")
  write()

  # This program displays the records that are
  # in the players.txt file.

  def read():

      # Open file to read
      with open("players.txt", "r") as pl_file:

          # Read the first line from the file, which is
          # the name field of the first record.
          name = pl_file.readline()

          # Loop that stops if there are no more names
          while name != "":
              #Read stats
              stat = pl_file.readline()

              #Strip the newlines from the field
              name = name.rstrip("\n")
              stat = stat.rstrip("\n")

              #Display the records.
              print(f"{name} ")
              print(f"{stat}")
              print()

              # Read the name of the next record
              name = pl_file.readline()
  read()
# Call main function
if __name__ == "__main__":
    main()
