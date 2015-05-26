#Converts each pdb entry in a directory into a multi FASTA format where each domain is a new FASTA entry. Good for alignments etc.

#A problem with the bioruby pdb sequence extractor was that it required an argument for which domain to convert to fasta. Here the conversion uses bioruby and then further parses to produce a FASTA with domains having their own FASTA entry without needing an argument.

#Gem for bioruby.
require 'bio'
time = Time.new

#This line sets the current directory as the one to convert pdbs.
path = Dir.pwd
Dir.glob("#{path}/*.pdb") do |pdb_file| #opens each pdb file in the folder and performs the below function on it.
  string = IO.read(pdb_file)
  structure = Bio::PDB.new(string)
  #This line is the title of the output. Usually it'll come out as "output_2015-05-25 02:18:37 +0100.fasta" or similar.
  output_file = "#{path}/output_#{time}.fasta"

  for domain in structure.seqres #The seqres currently holds several IDs and they don't properly print.
    titleline = ">#{structure.accession}_#{structure.definition}_Domain:"

    print titleline
    puts domain[0] #Holds the domain 'number' ie A or D or B or however you write your alphabet or whatever.
    puts domain[1] #Holds the actual sequence for the domain.
    puts

    #This is the actual content that is added to the file.
    content = "#{titleline} #{domain[0]}\n #{domain[1]}\n\n "
    File.open(output_file, 'a') { |file| file.write(content) }

  end

end
