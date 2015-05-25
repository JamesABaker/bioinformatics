#Converts each pdb entry in a directory into a multi FASTA format where each domain is a new FASTA entry.

#Gem for bioruby.
require 'bio'

time = Time.new
path = Dir.pwd

#Change this to the folder where your PDBs are being kept.
Dir.glob("#{path}/*.pdb") do |pdb_file| #opens each pdb file in the folder and performs the below function on it.

  filename = pdb_file
  string = IO.read(filename)
  structure = Bio::PDB.new(string)
  output_file = "#{path}/output_#{time}.fasta"

  for domain in structure.seqres #The seqres currently holds several IDs and they don't properly print.
    titleline = ">#{structure.accession}_#{structure.definition}_Domain:"

    print titleline
    puts domain[0] #Holds the domain 'number' ie A or D or B or however you write your alphabet or whatever.
    puts domain[1] #Holds the actual sequence for the domain.
    puts

    content = "#{titleline} #{domain[0]}\n #{domain[1]}\n\n "
    File.open(output_file, 'a') { |file| file.write(content) }

  end

end
