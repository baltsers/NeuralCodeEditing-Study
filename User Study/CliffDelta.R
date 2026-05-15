## #!/afs/nd.edu/user36/hcai/bin/R/Rscript

library(orddom)

args=commandArgs(trailingOnly=TRUE)
if (length(args)<1) {
	stop("too few arguments")
	exit
}
fndata=args[1]
print(paste("input file: ", fndata))

# read data in CSV format
mydata <- tryCatch({
	read.table(fndata, header=FALSE, sep=',')
}, warning = function(war) {
	print( paste("Warning: ", war) )
}, error = function(err) {
	print( paste("Error: ", err) )
	stop("bailed out now.")
}
)

# convert to matrix of numerics
m <- as.matrix (mydata[,0:2])

if (!is.numeric(m)) {
	stop("input data need be numeric")
}

m=t(m)
#print(m)

#orddom(m[1,],m[2,],alpha=0.05,paired=TRUE,studdist=FALSE,onetailed=TRUE,outputfile=paste(fndata,".cliff_delta",sep=""))
orddom(m[1,],m[2,],alpha=0.05,paired=FALSE,onetailed=TRUE,outputfile=paste(fndata,".cliff_delta",sep=""))

#orddom(m[1,],m[2,],alpha=0.05,paired=TRUE,outputfile=paste(fndata,".cliff_delta",sep=""))

#res=orddom(m[1,],m[2,],alpha=0.05,paired=TRUE,studdist=FALSE,onetailed=TRUE)
#print( res[7] ) # the delta value

#print("finished.")

# hcai: ts=4 sts=4 tw=4 
