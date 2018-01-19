#!/bin/bash

set -e

tol=0.01

if [ "$1" = "-t" ]; then
    shift
    tol=$1
    shift
fi

indir=raw
outdir=dataset

mkdir -p $outdir

if [ ! -d $indir ]; then
    mkdir $indir
    mv ~/vrep-pcl-*.pcd $indir
fi

for n in "bg" "dyn1"; do
    pcl_union_fast -t $tol $indir/vrep-pcl-${n}-*.pcd $outdir/$n.pcd
done
cp $indir/vrep-pcl-dyn2-0.pcd $outdir/scan.pcd

mv $outdir/{dyn1,s}.pcd

cd $outdir

pcl_intersection -t $tol s.pcd bg.pcd bg1.pcd
pcl_intersection -t $tol scan.pcd bg.pcd bg2.pcd
pcl_difference -t $tol scan.pcd bg.pcd dyn2.pcd
pcl_union -t $tol bg1.pcd bg2.pcd dyn2.pcd gt.pcd

