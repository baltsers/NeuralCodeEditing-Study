## #!/afs/nd.edu/user36/hcai/bin/R/Rscript

#require(xlsReadWrite)
#xls.getshlib()

args=commandArgs(trailingOnly=TRUE)
#print(length(args))
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
print(m)
if (!is.numeric(m)) {
	stop("input data need be numeric")
}

m=t(m)
#print(m)

#res <- 
wilcox.test(m[1,],m[2,],paired=FALSE,exact=FALSE,correct=TRUE,alternative="greater",conf.level=0.95,conf.int=TRUE)
#print( res[3] )
#print( res[8] )

#print("finished.")

# hcai: ts=4 sts=4 tw=4 
